import sys
import string
dlist = dict()
def userinp(d):

    while True:
        h = input("Enter file name: ")
        if len(h) < 1 : h = 'romeo-full.txt'

        try:
            hand = open(h)
            break
        except:
            print("File", h, "not found.")
            tryagain = input("\n\nTry again? Y or N: ---> ")
            if tryagain == 'y':
                continue
            elif tryagain == 'n':
                print("Exiting Program.")
                sys.exit()

    for line in hand:
        line = line.translate(line.maketrans('' , '', string.punctuation))
        line = line.lower()
        words = line.split()
        print(words)
        for w in words:
            d[w] = d.get(w,0) + 1

while True:
    ##fhand = input("Enter file name: ")
    ##if len(fhand) < 1 : fhand = 'clown.txt'
    userinp(dlist)
    tmp = list()
    tmp = sorted([(v,k) for k,v in dlist.items()],reverse=True)
    top = input("Enter desired number of lines returned: ")
    top = int(top)

    for val,key in tmp[:top]:
        print(key,val)

    rstrt = input("\n\nRun program again? Y or N ---> ")
    if rstrt == 'y' : continue
    elif rstrt == 'n' : print("Goodbye"), sys.exit()
