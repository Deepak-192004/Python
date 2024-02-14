perfect_number = int(input("Enter the number:"))
sum=0
for i in range(1,perfect_number):
    if (perfect_number % i== 0):
        sum = sum + i
if(sum==perfect_number):
      print("perfect number",perfect_number)
else:
    print("Not a perfect number",perfect_number)
