

repeat = True
while repeat:
    uinp = input("Enter a file name: ")
    if len(uinp) < 1 : uinp = 'mbox-short.txt'
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
        words = line.split()
        if len(words) < 2 or words[0] != 'From' : continue
        addr = words[1]
        uname, dom = addr.split('@')
        days[dom] = days.get(dom,0) + 1

    dlist = list()
    dlist = sorted([(v,k) for k,v in days.items()],reverse=True)
    for val,key in dlist:
        print(key, val)
    tagain = input(" Try Again? Y or N   ")
    if tagain == 'y' : continue
    elif tagain == 'n' :
        repeat = False
