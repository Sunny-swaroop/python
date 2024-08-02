#sum of 1 to "n" number
def Sum():
    num=int(input("enter a number:"))
    i=0
    t=0
    while i<=num:
        t=t+i
        i+=1
    return(t)
result =Sum()
print(f"the sum  is {result}")

