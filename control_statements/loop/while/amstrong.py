#check amstrong of a number
#using while loop
num=int(input("enter a number:"))
s=0
temp=num
while temp>0:
    result=temp%10
    s=s+(result*result*result)
    temp=temp//10
if(s==num):
        print(f"{num} is an amstrong number")
else:
        print(f"{num} is not an amstrong number")

