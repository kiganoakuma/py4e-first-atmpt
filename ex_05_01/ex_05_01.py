num = 0
tot = 0.0
while True :
    try:
        sval = input("Enter a number: ")
        if sval == 'done'  :
            print("done")
            avg = tot / num
            print(tot,num,avg)
            break
        fval = float(sval)
        num = num + 1
        tot = tot + fval
    except:
        print("Invalid input")
