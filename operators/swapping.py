#swapping of two numbes
#1st way
a=int(input("enter first number a:"))
b=int(input("enter second number b:"))
print(a,b)
c=a
a=b
b=c
print(a,b)



#2nd method of swapping
a=eval(input("enter first number a:"))
b=eval(input("enter second number b:"))
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)

