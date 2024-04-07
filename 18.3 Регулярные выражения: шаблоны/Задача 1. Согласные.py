import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

result = re.findall(r'\b[aeiouAEIOU]\w+', text)
print(result)
result = re.findall(r'\b[^aeiouAEIOU\W]\w*', text)
print(result)