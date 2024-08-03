#mapping function
#for every element present in sequence, apply some condition and
#Return the new sequence of elements for this purpose we use map 
#function.
 #syntax: filter(function, sequence)
#here first parameter function is for conditional check
#here second parameter sequence can be a list or tuple or set

#example multiplying with 2
#without lambda
def dbl(x):
 return 2*x
L=[2,3,4,5,6,7,8,9,10]
L1=list(map(dbl,L))
print(L1)



 
#with lambda
L=[2,3,4,5,6,7,8,9,10]
L1=list(map(lambda x:2*x,L))
print(L1)

