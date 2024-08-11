# findall ==> list of strings
#example
import re
pattern=r"Python"
text="python is a scripting language .we are learning python"
match_list=re.findall(pattern,text)
for match in match_list:
    print(match)
if len(match_list)==0:
    print(pattern,"Found")
	

