#variable length positional arguements:

def add(*arg):
    print(type(arg))
    print("Number of arguements",len(arg))
    print("Arguement list is",)
    s=0
    for i in arg:
        s=s+i
    return s
a=10
b=20
c=add(a,b)
print("Sum of {} and {} is {}".format(a,b,c))
c=add(10,20,30,40,50)
print("Sum is",c)
c=add(100)
print("Sum is",c)
