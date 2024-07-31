#minimum of 3 numbers
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
if num1<num2 and num1<num3:
    print(f"the {num1} is minimum  number")
elif num2<num3:
    print(f"the {num2} is minimumm number")
else:
    print(f"the {num3} is minimum number")

