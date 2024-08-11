#subn: Replaces all occurrences of the pattern in the string with a replacement string and gives number of occurances
import re
text = "I love apples. Apples are delicious."
# Replace all occurrences of "apples" with "bananas"
result = re.subn(r'apples', 'bananas', text, flags=re.IGNORECASE)
print(result)
# Output: "I love bananas. Bananas are delicious.2"

