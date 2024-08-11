#search()
#search will give first occurance and returns None or match object
#example
import re
pattern=r"python"
text="we are learning python"
match=re.search(pattern,text)
if match!=None:
    print(match.start(),match.end(),match.group())
else:
	print(pattern,"Is not Found")

