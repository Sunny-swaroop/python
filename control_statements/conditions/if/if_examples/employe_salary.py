#employe salary
 name=input("enter your name:")
 employe_id=int(input("enter your id:"))
 basic_salary=int(input("enter your basic salary amount:"))
 if basic_salary <= 30000:
      hra=(basic_salary*(20/100))
      print(f"the HRA is {hra}")
      da=(basic_salary*(10/100))
      print(f"the DA is {da}")
      income_tax=(basic_salary*(5/100))
      print(f"the income tax is {income_tax}")
 elif basic_salary <= 50000:
      hra=(basic_salary*(25/100))
      print(f"the HRA is {hra}")
      da=(basic_salary*(15/100))
      print(f"the DA is {da}")
      income_tax=(basic_salary*(10/100))
      print(f"the income tax is {income_tax}")
 elif basic_salary <= 100000:
      hra=(basic_salary*(35/100))
      print(f"the HRA is {hra}")
      da=(basic_salary*(20/100))
      print(f"the DA is {da}")
      income_tax=(basic_salary*(15/100))
      print(f"the income tax is {income_tax}")
 elif basic_salary>100000:
      hra=(basic_salary*(40/100))
      print(f"the HRA is {hra}")
      da=(basic_salary*(25/100))
      print(f"the DA is {da}")
      income_tax=(basic_salary*(20/100))
      print(f"the income tax is {income_tax}")
 else:
      print(f"{name},{employe_id} please check your details")
 gross_salary=basic_salary+hra+da
 net_salary=gross_salary-income_tax
 print(f"the gross salary {name} is {gross_salary}")
 print(f"the net salary {name} is {net_salary}")


