#pattern printing 1 to n value
#using for loop
y=int(input("enter the value of y :"))
for i in range(1,y+1):
    for j in range(i):
        print(j,end=" ")
    print()

