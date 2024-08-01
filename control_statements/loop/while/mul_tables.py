#multliplication tables upto n
#using while loop
num=int(input("enter a  number :"))
i=1
while i<=num:
    j=1
    while j<=10:
        r=i*j
        print(f"{i} * {j} = {r}")
        j+=1
    print(" ")
    i+=1
