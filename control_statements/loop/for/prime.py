#prime numbers checking
#using for loop

num=int(input("enter the number to check:"))
p=0
for i in range(1,num+1):
    z=num%i
    if z==0:
        p+=1
if p==2:
    print(f"the number {num} is a prime number")
else:
    print(f"the number {num} is not a prime number")

