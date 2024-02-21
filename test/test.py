
import re
import string
repeat = True
while repeat:
    uinp = input("Enter a file name: ")
    if len(uinp) < 1 : uinp = 'mbox.txt'
    if uinp == 'done' :
        repeat = False
        print("Exiting")
        break
    days = dict()
    try:
        fopen = open(uinp)
    except:
        print("File not found.")
        continue

    print("\n\nFILE OPENED:", uinp, "\n\n")

    for line in fopen:
            f = re.findall('^From .*@([^ ]*)', line)
            if len(f) >= 1 :
                addr = f[0]
                addr = addr.translate(addr.maketrans('','', '><:;(){[]},'))
                days[addr] = days.get(addr,0) + 1

    dlist = list()
    dlist = sorted([(v,k) for k,v in days.items()],reverse=True)
    print("Top 10 Recipients:\n------------------\n")
    for k,v in dlist[:10]:
        print(v,k,"\n")
