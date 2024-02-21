uwords = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for w in words:
        if w in uwords :
            continue
        elif w not in uwords :
            uwords.append(w)
            continue
uwords.sort()
print(uwords)
