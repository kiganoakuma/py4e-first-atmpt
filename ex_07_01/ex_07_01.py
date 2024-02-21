
# print(fh)

# search = input("Enter a search:")
fh = open('mbox-short.txt')
count = 0
fnum = 0

while True :
    s = input("Enter a search:")
    if s == 'done' :
        print("done")
        break
    for line in fh:
        if line.startswith(s):
            snum = line.lstrip('X-DSPAM-Confidence: ')
            # print(snum)
            fnum = float(snum) + fnum
            count = count + 1

    print("Average spam confidence:",fnum /count)
