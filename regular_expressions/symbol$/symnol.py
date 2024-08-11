#Symbol:
#it is denoted with "$"
#We can use "$" symbol to check whether the given target string ends 
#with our provided pattern or not.
#Ex: 
import re
s="Learning Python is Very Easy"
m=re.search("Easy$",s)
if m != None:
 print("Target String Ends with Easy")
else:
 print("Target String Not Ends with Easy")

