# sub:  Replaces all occurrences of the pattern in the string with a replacement string.
import re
text = "I love apples. Apples are delicious."
# Replace all occurrences of "apples" with "bananas"
result = re.sub(r'apples', 'bananas', text, flags=re.IGNORECASE)
print(result)
# Output: "I love bananas. Bananas are delicious."


