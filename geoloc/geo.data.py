import sqlite3
import ssl
import http
import urllib.parse, urllib.error, urllib.request
import time
import sys
import json

repeat = True
while repeat:

    api_key = False

    if api_key is False:
        api_key = 42
        serviceurl = "http://py4e-data.dr-chuck.net/json?"
    else:
        serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

    deskpath = '/Users/devil/desktop/py4e_databases/'
    dataname = 'geolocations.db'
    datapath = deskpath + dataname
    conn = sqlite3.connect(datapath)
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    fh = open('where.data')
    count = 0
    for line in fh:
        if count > 10:
            print('COUNT =',count)
            print("RATE LIMIT REACHED, RESTART TO CONTINUE>")
            reset = True
            while reset : 
                res = input("\n\nRESART NOW? Y or N > ")
                if res.lower() not in ['y', 'n'] :
                    print('\n\n====Invalid Responce====')
                    continue
                else : 
                    repeat = False
                    break
                   
            if res.lower() == 'y' :
                count = 0
                geod = None
                continue
            elif res.lower() == 'n' :
                repeat = False
                break
        address = line.strip()
        print(' ')
        cur.execute("SELECT geodata FROM Locations WHERE address = ?",
                    (memoryview(address.encode()), ))

        try:
            geod = cur.fetchone()[0]
            print("Found in database..", address)
            continue
        except:
            pass
        
        parms = dict()
        parms['address'] = address
        if api_key is not False : parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving...', url )
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
        count = count + 1

        try:
            js = json.loads(data)
        except:
            print(data)
            continue
        
        if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
            print('=====FAILED TO RETRIEVE=====')
            print(data)
        
        cur.execute('''INSERT OR IGNORE INTO Locations (address, geodata) 
                    VALUES ( ?, ? ) ''', ( memoryview(address.encode()), memoryview(data.encode()) ) )
        conn.commit()
        if count % 10 == 0 :
            print('\nPausing...\n\nCOUNT =', count)
            time.sleep(3)
    repeat = False