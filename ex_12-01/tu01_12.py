import socket
import string
wdic = dict()
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    mystring = data.decode()
    print(mystring)
    wrds = mystring.split()
    for w in wrds:
        wdic[w] = wdic.get(w,0) + 1

    
mysock.close()

print(wdic)

##for line in mystring:
##    wrds = line.split()
##    for wrd in wrds:
##        wdic[wrd] = wdic.get(wrd,0) + 1
##print("************")
##print(wrds)
##print()
##tmp = ("***********")
##tmp = sorted([(k,v)for v,k in wdic.items()],reverse=True)
##for v,k in tmp:
##    print(k,v)

        
