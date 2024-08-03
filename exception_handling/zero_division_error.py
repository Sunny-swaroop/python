#exception handling

#method 1

try:
    num1=11
    num2=3
    print(num1/num2)   #the output be like 3.666
except Exception as e:
    print("divison by zero not possible")
else:
    print("divison successful") #the divison successful
finally:
    print('finally execute the problem') #finally execute the problem    






#method 2
try:
    num1=10
    num2=0
    print(num1/num2)
except Exception as e:
    print("division by zero not possible")#output be like division by zero not possible
else:
    print("divison successful") 
finally:
    print('finally execute the problem')  #finally execute the problem  






