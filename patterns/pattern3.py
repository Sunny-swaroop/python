#3rd example
#printing alphabets
 u=int(input("enter the value of u :"))
 ascii_value=97
 for i in range(1,u+1):
      for j in range(i):
          print(chr(ascii_value + j),end="  ")
      print()

