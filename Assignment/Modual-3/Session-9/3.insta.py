import re
text = "#shorts #viral #ai #2026goals"

def extract_hashtags(text):
    insta = re.findall("#\w*",text)
    print(insta)

extract_hashtags(text)