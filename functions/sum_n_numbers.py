
#sum of 1 to "n" numbers
#using recursion function
def Sum1(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        s=n+Sum1(n-1)
        return s
n=int(input("enter the number:"))
result=Sum1(n)
print(f"the sum of {n} = {result}")

