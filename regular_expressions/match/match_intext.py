
# match()it returns match object when the pattern finds at starting else None
#example
import re
pattern=r"python"
text="python is easy to learn we are learning python"
return_obj=re.match(pattern,text)
if return_obj!=None:
    print(return_obj.start(),return_obj.end(),return_obj.group())
else:
	print(pattern,"not Found")


