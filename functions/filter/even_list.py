#using filter
#it is used to used to filter a sequence (like a list, tuple, or set) based on a given function that tests each element in the sequence.
#It returns an iterator that produces elements of the sequence for which the function returns True.
#solving with function
#even number or not
def even(num):
    return num%2==0
num=int(input("enter the number:"))
num=list(range(1,num+1))
print(num)
t=filter(even,num)
result=list(t)
print(result)


#using lambda function
#using filter method
l=[]
n=int(input("enter a number:"))
for i in range(1,n+1):
    l.append(i)
    i+=1
print(l)
flt=list(filter(lambda n:n%2==0,l))
print(flt)

