sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)
# print(fh, fr)
if fh > 40 :
    reg = fh * fr
    otp = (fh - 40) * (fr * 1.5)
    tp = reg + otp
    # print("Regular pay:",reg)
    # print("Overtime pay:",otp)
    print("pay:",tp)
else:
    xp = fh *  fr
    print("pay:",xp)
