
#tuple data type
tuple1=(1,2,3,4,5,6,7,8,9,10)
print(tuple1)
print(type(tuple1))

#form the keyboard entering the tuple
list3=[]#first we have to enter the values in list 
number=int(input("enter the value:"))
for i in range(1,number+1):
    list3.append(i)
print(list3)
print(type(list3))
tuple2=tuple(list3)#and then we can convert into tuple ,directly we cannot assign the values through keyboard
print(tuple2)
print(type(tuple2))
    
