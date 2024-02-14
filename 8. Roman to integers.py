d={'':0,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s=input("Enter the roman numbers :")
result=0
current=0
prev=0
for c in s[::-1]:
    current=d[c]
    if current<prev:
            result-=current
    else:
        result+=current
        prev=current
print(result)
