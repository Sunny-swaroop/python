#Module is for reusability of the program code into other program.
#Once we write logic in one program that logic we can use into any other 
#program by importing the program name as module
#1st type 
from sample1 import *
num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
result=add(num1,num2)
print(result)
result1=sub(num1,num2)
print(result1)
result2=multiply(num1,num2)
print(result2)
result3=div(num1,num2)
print(result3)



#2nd type
import sample1
num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
result=add(num1,num2)
print(result)
result1=sub(num1,num2)
print(result1)
result2=multiply(num1,num2)
print(result2)
result3=div(num1,num2)
print(result3)


#3rd type
from sample1 import add
num1=int(input("enter a first number:"))
num2=int(input("enter a second number:"))
result=add(num1,num2)
print(result)




