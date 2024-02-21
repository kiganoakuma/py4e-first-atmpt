d = dict()
fhand = open('words.txt')
count = 0
for line in fhand:
    words = line.split()
    for w in words:
        d[w] = d.get(w,count)
        count = count + 1

print(d)
