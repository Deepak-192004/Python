amount=int(input("Enter the income amount="))
if amount<=150000:
    print("No tax")
elif amount<=150001 and 300000>=amount:
    print("10% tax charge")
    tax_amount=(10/100)*amount
    print("total tax amount=",tax_ampont)
elif amount<=300001 and 500000>=amount:
    print("20% tax charge")
    tax_amount=(20/100)*amount
    print("total tax amount=",tax_amount)
else:amount>=500000
print("30% tax charge")
tax_amount=(30/100)*amount
print("total tax amount=",tax_amount)
