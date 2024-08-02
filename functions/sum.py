#functions
#no argument and no return type
# sum of two numbers

def Sum():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    sum1=num1+num2
    print(f" the sum of {num1} + {num2} = {sum1}")

Sum()


#with argument and no return type
def Sum1(num1,num2):
    sum2=num1+num2
    print(f"the sum of {num1} + {num2} = {sum2}")

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
Sum1(num1,num2)


#with argument and return type
def Sum2(num1,num2):
    sum3=num1+num2
    return (sum3)
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
result=Sum2(num1,num2)
print(f"the sum of {num1} + {num2} = {result}")


#no argument and return type
def Sum3():
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    sum4=num1+num2
    return(sum4)
result=Sum3()
print(f"the sum of {num1} + {num2} = {result}")





