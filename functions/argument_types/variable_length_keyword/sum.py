#variable length keyword arguements
def add(**arg):
    print(type(arg))
    print("Number of arguements",len(arg.keys()))
    print("Arguement list is",arg)
    s=0
    keys_list=arg.keys()
    print("Keys:",keys_list)
    for each_key in keys_list:
        s=s+arg[each_key]
    return s
a=10
b=20
c=add(a=10,b=20)
print("Sum of {} and {} is {}".format(a,b,c))
c=add(a=10,b=20,c=30,d=40,e=50)
print("Sum is",c)
c=add(a=100)
print("Sum is",c)

