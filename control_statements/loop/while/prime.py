#checking prime numbers
#using while loop
num=int(input("enter the number:"))
i=1
p=0
while i<=num:
    z=num%i
    i+=1
    if z==0:
        p+=1
if p==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


