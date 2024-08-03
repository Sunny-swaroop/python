#reduce function
#Reduce () function reduces sequence of elements into a single element by 
#applying the specified function.
#syntax: filter(function, sequence)
#Reduce () function present in functools module and hence we should write 
#import statement
#sum of x,y in the list.
from functools import reduce
def f1(x,y):
 return x+y
L=[10,20,30,40,50,60,70]
result=reduce(f1,L)
print(result)



#using lambda function
from functools import reduce
L=[10,20,30,40,50,60,70]
result=reduce(lambda x,y:x+y,L)
print(result)

