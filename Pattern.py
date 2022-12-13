n=int(input("Enter the number of rows"))

for i in range(0,n+1):
    for j in range(1,i):
        print("*",end=" ")
    print()

for i in range(n-1,1,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()

for i in range(0,n):
    for j in range(0,i):
        print(i,end=" ")
    print()

for i in range(0,n+1):
    for j in range(1,i):
        print(j,end=" ")
    print()
