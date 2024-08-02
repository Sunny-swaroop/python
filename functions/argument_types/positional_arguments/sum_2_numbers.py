
#positional Arguements
#a positional argument is a type of argument that is passed to a function in a specific position. The order in which you provide these arguments matters, as each positional argument is matched to the corresponding parameter in the function definition.
def add(x,y):
    z=x+y
    return z
a=10
b=20
c=add(a,b)
print("Sum of {} and {} is {}".format(a,b,c))

