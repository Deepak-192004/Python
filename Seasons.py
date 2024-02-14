month=input("Enter the month")
date=int(input("Enter the date"))
if month in ("January","February","March"):
    print("Summer Season")
elif month in ("April","May","June"):
    print("Spring Season")
elif month in ("July","August","September"):
    print("Autumn Season")
else:
    print("Winter Season")
if(month=="March")and(date>20):
    print("Summer Season")
elif(month=="June")and(date>21):
    print("Spring Season")
elif(month=="September")and(date>22):
    print("Autumn Season")
elif(month=="December")and(date>21):
    print("Winter Season")
