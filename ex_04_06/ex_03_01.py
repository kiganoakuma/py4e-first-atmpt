def computepay(hours, rate) :
    # print("In computepay",hours,rate)
    if hours> 40 :
        reg = hours * rate
        otp = (hours - 40) * (rate * 1.5)
        pay = reg + otp
    else:
        pay = hours *  rate
    # print("Returning:",pay)
    return pay

sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)

print("Pay",xp)
