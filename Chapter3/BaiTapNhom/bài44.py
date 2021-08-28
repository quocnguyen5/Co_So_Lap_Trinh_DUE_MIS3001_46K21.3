month, date = [str(c) for c in input("").split(" ")]
if month == "January" and date == "1":
    print("New year's day")
elif month == "July" and date == "1":
    print("Canada day")
elif month == "December" and date == "25":
    print("Christmas day")
else:
    print("Not correspond to a fixed-date holiday")

