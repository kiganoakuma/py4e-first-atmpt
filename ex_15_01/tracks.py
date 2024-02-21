import xml.etree.ElementTree as ET
import sqlite3
from tabulate import tabulate
deskpath = '/Users/devil/desktop/py4e_databases/'
dataname = 'AppleLibrary.db'
datapath = deskpath + dataname
conn = sqlite3.connect(datapath)
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    len INTEGER, count INTEGER
);
''')


fname = input('ENTER FILE NAME: ')
if len(fname) < 1 : fname = 'AppleLibrary.xml'

def lookup(d, key):
    found = False
    for child in d:  
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    
    if ( lookup(entry, 'Track ID') is None ) : continue
    
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    length = lookup(entry, 'Total Time')

    if name is None or artist is None or album is None : continue

    # print(name, artist, album, count)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist, ))

    cur.execute('''SELECT id FROM Artist Where name = ? ''', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (artist_id, title) VALUES ( ?, ? )''', (artist_id, album))

    cur.execute('''SELECT id FROM Album WHERE title = ?''',(album,))
    album_id = cur.fetchone()[0]
    cur.execute('''INSERT OR IGNORE INTO Track (title, album_id, len, count)
                VALUES ( ?,  ?, ?, ? )''',(name, album_id, length, count,))
    
    conn.commit()

query = ('''
        SELECT Artist.name, Album.title, Track.title, Track.len, Track.count
        FROM Artist JOIN Album JOIN Track ON Artist.id = Album.artist_id AND Album.id = Track.album_id
        ORDER BY Artist.name
    ''')
cur.execute(query)
data = cur.fetchall()
headers = ('ARTIST', 'ALBUM', 'TITLE', 'LENGTH', 'PLAY COUNT')

print(tabulate(data, headers=headers, tablefmt='fancy'))