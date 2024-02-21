fhand = open('mbox-short_test.txt')
count = 0
for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) <= 1 or words[0] != 'From' : continue
    print(words[2])
