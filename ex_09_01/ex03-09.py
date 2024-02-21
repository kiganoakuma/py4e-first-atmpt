uinp = input("Enter a file name: ")
if len(uinp) < 1 : uinp = 'mbox-short.txt'
days = dict()
try:
    fopen = open(uinp)
except:
    print("File not found.")
    exit()
print("FILE OPENED:", uinp)
for line in fopen:
    words = line.split()
    if len(line) < 3 or words[0] != 'From' : continue
    days[words[1]] = days.get(words[1],0) + 1
dlist = list()
dlist = sorted([(v,k) for k,v in days.items()],reverse=True)
print("\n\n\n          SORTED DATA\n\n")
for val,key in dlist:
    print("Recipiant: ",key,"\nNumber of Emails: ",val,"\n------------------------------------------")
print("\n\n\n")
