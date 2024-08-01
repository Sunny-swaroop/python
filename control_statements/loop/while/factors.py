#factors of a number
#using while loop
num1=int(input("enter a number to find out the factors:"))
i=1
while i<=num1:
    if num1%i==0:
        print(i,end="\t")
    i+=1

