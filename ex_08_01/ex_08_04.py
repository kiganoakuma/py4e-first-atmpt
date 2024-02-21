fhand = open('mbox-short_test.txt')
count = 0
days = dict()
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) <= 1 or words[0] != 'From' : continue
    print(words)
print(days)
