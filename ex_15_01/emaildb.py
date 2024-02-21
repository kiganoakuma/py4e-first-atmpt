import sqlite3
from tabulate import tabulate
deskpath = '/Users/devil/Desktop/'
dataname = 'Emaildb.db'
datapath = deskpath + dataname
conn = sqlite3.connect(datapath)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, email TEXT, count INTEGER)''')

cur.execute('DROP TABLE IF EXISTS Spam')

cur.execute('''
CREATE TABLE Spam (email_id INTEGER, confidence FLOAT)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
email = None
for line in fh:
    if line.startswith('From:') :
        pieces = line.split()
        email = pieces[1]
        cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (email, count)
                    VALUES (?, 1)''', (email,)) 
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
        continue
    elif line.startswith('X-DSPAM-Confidence:') :
        pieces = line.split()
        scon = pieces[1]
        cur.execute('SELECT id FROM Counts WHERE email = ?', (email,))
        idcol = cur.fetchone()
        emailid = idcol[0]
        cur.execute('SELECT confidence FROM Spam WHERE confidence = ? ', (scon,))
        cur.execute('''INSERT INTO Spam (email_id,confidence)
                VALUES (?,?)''', (emailid, scon))
    else : continue
    conn.commit()


# https://www.sqlite.org/lang_select.html
sqlstr = '''
SELECT Counts.email, Spam.confidence, Counts.count 
FROM Counts JOIN Spam on 
Counts.id = email_id ORDER BY count DESC LIMIT 10
'''

headers = ['Email', 'Confidence', 'Count']

cur.execute(sqlstr)

rows = cur.fetchall()

print(tabulate(rows, headers=headers, tablefmt='pipe'))

cur.close()
