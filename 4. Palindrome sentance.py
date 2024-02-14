a=input("enter the stirng")
c=""
a=a.lower()
for i in range(len(a)):
     if a[i]==" " or a[i]=="." or a[i]=="," or a[i]==":":
          continue
     else:
          c=c+a[i]
print(c)

if c==c[::-1]:
     print("Pallindrome")
else:
     print("not a pallindrome")
