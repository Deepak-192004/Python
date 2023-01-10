month=input("Enter the Month")
date=int(input("Enter the Date"))
if month in ("January","February","March"):
    print("summer Season")
elif month in ("April","May","June"):
    print("Spring Season")
elif month in ("july","August","September"):
    print("Autumn season")
else:
    print("Winter Season")
if(month=="March")and(date>20):
    print("summer Season")
elif(month=="June")and(date>21):
    print("Spring Season")
elif(month=="September")and(dete>22):
    print("Autumn Season")
elif(month=="December")and(date>21):
    print("Winter Season")
