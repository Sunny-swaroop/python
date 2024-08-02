#factorial of n number
#using recursion function
def factorial(num):
    if num==0:
        return 1
    elif num==1:
        return 1
    else:
        f=num*factorial(num-1)
    return f
num=int(input("enter a number:"))
result=factorial(num)
print(f"the factorial of {num} is {result}")

