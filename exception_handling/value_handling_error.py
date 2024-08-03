
# value error handling

try:
    num1="str"
    num2=99
    print(num1+num2)
except Exception as e:
    print("enter the correct value") #output be like enter the correct value
else:
    print("the execution is successful")
finally:
    print('finally executed the program') #finally executed the program





#2nd type


try:
    num1=101
    num2=99
    print(num1+num2)
except Exception as e:
    print("enter the correct value") 
else:
    print("the execution is successful")#output be like the execution is successful
finally:
    print('finally executed the program') #finally executed the program



