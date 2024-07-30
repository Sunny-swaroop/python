#list functions
#slice function
#A slice object is used to specify how to slice a sequence.
#You can specify where to start the slicing, and where to end. You can also specify the step.
#syntax for slice() is [start:stop:step]
    #start():it indicates the index value, where it has to start.
    #stop():it indicates the index,where it has to end
    #step() : it indicates the increment value

list2=[]             
num=eval(input("enter the value :"))     #if we give value 15
for i in range(1,num+1):
    list2.append(i)
print(list2)             #list2 is updated with 1 to 15 numbers
#using slice method we can print the increment of 2 upto num
print(list2[0:num:2])
            #zero will be default index value.
print(list2[:num:2])
            #the output will be [1,3,5,7,9,11,13,15]                            

