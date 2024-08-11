#regular expressions
# A RegEx, or Regular Expression, is a sequence of characters that 
#forms a search pattern.
#RegEx can be used to check if a string contains the specified search 
#pattern.
# Python has a built-in package called re, which can be used to work 
#with Regular Expressions.
#If we want to represent a group of Strings according to a particular 
#format/pattern then we should go for Regular Expressions. 
#Regular Expressions is a declarative mechanism to represent a group 
#of Strings according to particular format/pattern.
#The main important application areas of Regular Expressions are :
# 1)To develop validation frameworks/validation logic 
# 2) To develop Pattern matching applications.
#re module contains several inbuilt functions to use Regular 
#Expressions very easily in our applications.
#example
import re
i=0
pattern=re.compile("ab") 
match=pattern.finditer("abaaababa")
for m in match:
    i+=1
print(m.start(),m.end(),m.group())
print("the number of occurrences:",i)


#compile () : This function is used to compile a pattern into Regex 
#Object. 
#finditer(): Returns an Iterator object which , Match object for every 
#Match 
#On Match object we can call the following methods. 
#1. start() : Returns start index of the match
#2. end() : Returns end+1 index of the match
#3. group() : Returns the matched string
