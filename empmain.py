import employee

name = input("Enter Name :")
basic = float(input("Enter salary :"))

da=employee.DA(basic)
hra=employee.HRA(basic)
pf=employee.PF(basic)

gross=basic+da+hra
itax=employee.ITAX(gross)
net=gross-(pf-itax)

print("Employee name :",name)
print(f"basic salary :{basic}")
print(f"DA(10%) :{da}")
print(f"HRA(15%) :{hra}")
print(f"PF(12%) :{pf}")
print(f"Itax(8%) :{itax}")
print(f"Gross Salary :",gross)
print(f"Net Salary:",net)
