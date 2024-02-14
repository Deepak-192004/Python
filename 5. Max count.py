n=int(input("Enter the number of items in list:"))
L1=[]
for i in range(n):
    a=int(input("Enter the number"))
    L1.append(a)
print(L1)
count=0

L2=[]
for i in L1:
    count=0
    min=i
    for j in L1:
        if min>j:
            count=count+1
        else:
            continue
    L2.append(count)
print(L2)
