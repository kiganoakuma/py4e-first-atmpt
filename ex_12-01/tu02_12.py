import urllib.request, urllib.parse, urllib.error
wdic = dict()
addr = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in addr:
        wrds = (line.decode().split())
        for wrd in wrds:
            wdic[wrd] = wdic.get(wrd,0) + 1


tmp = list()
tmp = sorted([(k,v)for v,k in wdic.items()],reverse=True)
for v,k in tmp:
    print(k,v)

        
