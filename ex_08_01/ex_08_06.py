t = []
while True :
    s = input("Enter a number: ")
    if s == 'done' :
        break
    fs = float(s)
    t.append(fs)
print("Maximum:",max(t))
print("SMinimum:",min(t))
