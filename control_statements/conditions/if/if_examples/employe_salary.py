#employe salary
name=input("enter your name:")
employe_id=int(input("enter your id:"))
basic_salary=int(input("enter your basic salary amount:"))
if basic_salary==0:
    print(f"{name},{employe_id} enter your valid salary to check ")
elif basic_salary <= 30000:
    hra=(basic_salary*(20/100))
    da=(basic_salary*(10/100))
    income_tax=(basic_salary*(5/100))
    gross_salary=basic_salary+hra+da
    net_salary=gross_salary-income_tax
    print(f"{name},{employe_id} your salary of this month is {net_salary}")
elif basic_salary > 30000 and basic_salary <= 50000:
    hra=(basic_salary*(25/100))
    da=(basic_salary*(15/100))
    income_tax=(basic_salary*(10/100))
    gross_salary=basic_salary+hra+da
    net_salary=gross_salary-income_tax 
    print(f"{name},{employe_id} your salary of this month is {net_salary}")
elif basic_salary > 50000 and basic_salary <= 100000:
    hra=(basic_salary*(35/100))
    da=(basic_salary*(20/100))
    income_tax=(basic_salary*(15/100))
    gross_salary=basic_salary+hra+da
    net_salary=gross_salary-income_tax
    print(f"{name},{employe_id} your salary of this month is {net_salary}")
elif basic_salary>100000:
    hra=(basic_salary*(40/100))
    da=(basic_salary*(25/100))
    income_tax=(basic_salary*(20/100))
    gross_salary=basic_salary+hra+da
    net_salary=gross_salary-income_tax
    print(f"{name},{employe_id} your salary of this month is {net_salary}")
else:
    print(f"{name},{employe_id} please check your details")


