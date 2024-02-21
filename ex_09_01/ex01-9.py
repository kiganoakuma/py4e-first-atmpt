wdict = dict()
fhand = open('words.txt')
count = 0
for line in fhand:
    words = line.split()
    for w in words:
        if w in wdict :
            continue
        elif w not in wdict :
            wdict.update({w : count})
            count = count + 1
            continue
print(wdict)
