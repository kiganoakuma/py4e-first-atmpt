sh = input("Enter hours: ")
sr = input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, Not a number\n program restarted")
    if fh > 40 :
        reg = fh * fr
        otp = (fh - 40) * (fr * 1.5)
        tp = reg + otp
        print("pay:",tp)
    else:
        xp = fh *  fr
        print("pay:",xp)