#reverse a number
#using while loop
num1=int(input("enter a 2-digit,3-digit,4-digit or more number:"))
reverse=0
number=num1
while number>0:
    last=number%10
    reverse=reverse*10+last
    number=number//10   
print(f"the reverse number is {reverse}")

