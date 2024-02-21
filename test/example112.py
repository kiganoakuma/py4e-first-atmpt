import string

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

d = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('','', string.punctuation))
    ine = line.lower()
    words = line.split()
    for w in words:
        d[w] = d.get(w,0) + 1

print(d)
