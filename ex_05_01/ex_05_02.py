big = None
while True :
    sval = input("Enter a number: ")
    if sval == 'done' :
        print("Largest int inp",big)
        print("done")
        break
    try :
        fval = float(sval)
    except :
        print("Invalid input")
    if big is None or fval < big :
        big = fval
