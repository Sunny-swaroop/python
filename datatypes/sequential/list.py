#list data type
list1=[1,2,3,4,5,6,7,8,9,10]#to define list we have to use '[]'
print(list1)
print(type(list1))



#from the keyboard entering the list using for while
list2=[]
number=int(input("enter the numbers :"))
for i in range(1,number+1):
    list2.append(i)
print(list2)
