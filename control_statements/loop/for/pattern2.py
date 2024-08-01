# printing the pattern              #output will be:1 
                                                   #2 2 
                                                   #3 3 3 
                                                   #4 4 4 4 
                                                   #5 5 5 5 5 
         
#using for loop
#pattern 2
num=int(input("enter a number:"))
for i in range(1,num+1):
    print(f"{i} "*i)
