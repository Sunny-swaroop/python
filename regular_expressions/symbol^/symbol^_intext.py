#Symbol:
#it is denoted with "^"
#We can use ^ symbol to check whether the given target string starts 
#with our provided pattern or not. 
#Ex: 
import re
s="Learning Python is Very Easy"
m=re.search("^Learn",s)
if m != None:
 print("Target String starts with Learn")
else:
 print("Target String Not starts with Learn")


