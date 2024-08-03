#reduce function
#Reduce () function reduces sequence of elements into a single element by 
#applying the specified function.
#syntax: filter(function, sequence)
#Reduce () function present in functools module and hence we should write 
#import statement
#subtraction of x,y in the list.
from functools import reduce
def sub(x,y):
 return x-y
L=[1,10,20,2,5,50]
result=reduce(sub,L)
print(result)



#using lambda function
from functools import reduce
L=[1,10,20,2,5,50]
result=reduce(lambda x,y:x-y,L)
print(result)

