#split()
#If we want to split the given target string according to a particular 
#pattern then we should go for split() function.
#example

import re
text = "I love apples. Apples are delicious."
result = re.split(r' ',text)
print(result)
#output:
#['I', 'love', 'apples.', 'Apples', 'are', 'delicious.']

