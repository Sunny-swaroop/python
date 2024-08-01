#fibanancii series
#using while loop
num=int(input("enter a number:"))
a=0
b=1
i=0
while i<(num-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    i+=1
    
