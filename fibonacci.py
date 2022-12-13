N=int(input("Enter the number"))
a=int(input("Enter the a value:"))
b=int(input("Enter the b value:"))
print(a)
print(b)
for i in range(0,10):
    c=a+b
    print(c)
    a=b
    b=c
    
