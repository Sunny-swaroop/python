#functions
#no argument and no return type
# area of a rectangle

def Area():
    length=int(input("enter the length value :"))
    breadth=int(input("enter the breadth value:"))
    area=length*breadth
    print(f" the area of rectangle is {area}")

Area()


#with argument and no return type
def Area1(length,breadth):
    area1=length*breadth
    print(f"the area of rectangle is {area1}")


length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
Area1(length,breadth)


#with argument and return type
def Area2(length,breadth):
    area2=length*breadth
    return (area2)
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
result=Area2(length,breadth)
print(f"the area of rectangle is {result}")


#no argument and return type
def Area3():
    length=int(input("enter the length value :"))
    breadth=int(input("enter the breadth value:"))
    area3=length*breadth
    return(area3)
result=Area3()
print(f"the area of rectangle is {result}")





