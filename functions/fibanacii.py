#fibanancii series
#using recursion series
def Fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        n=Fib(n-1)+Fib(n-2)
    return (n)
n=int(input("enter a number:"))
for x in range(n+1):
    res=Fib(x)
    print(res,end=" ")
    
