#polindrum number
num=input("enter a number:")
i=1
n=1
while i<=n:
    if num==num[::-1]:
        print(f"{num}is a palindrome")
    else:
        print(f"{num} not a palindrome")
    i+=1

