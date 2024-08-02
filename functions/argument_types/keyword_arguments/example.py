#keyword Arguements we can change the order of the paramters

def add(x,y):
    z=x+y
    return z
a=10
b=20
c=add(y=a,x=b)
print("Sum of {} and {} is {}".format(a,b,c))

