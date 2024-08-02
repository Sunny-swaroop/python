#power program
#using recursion function
def power(x,n):
    if n==0:
        return 1
    else:
        result=x*power(x,(n-1))
        return result
x=int(input("enter a number :"))
n=int(input("enter a number :"))
s=power(x,n)
print(s)

