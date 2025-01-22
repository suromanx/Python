text = 'KJDfkjndKJDFNLkdkfkd'
new_text = ''
for i in text:
   if i.isupper():
       new_text+=i.lower()
   if i.islower():
       new_text +=i.upper()

print(new_text)