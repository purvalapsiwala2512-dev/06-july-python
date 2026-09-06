import re

st = "Sun rises in east in"

# k = re.match("Sun",st)
# k = re.search("in",st)
# k = re.findall("in",st)
# k = re.finditer("in",st)
# print(next(k))
# print(k)

# k = re.sub("in","K",st)
# k = re.split(" ",st)
# print(k)

st = "a quick foxx brown foox jump fx over the lazy dog 323 rer 55"

# k = re.findall("f.x",st)
# k = re.search("^fox",st)
# k = re.search("dog$",st)
# k = re.findall("fo*x",st)
# k = re.findall("fo+x",st)
# k = re.findall("fo?x",st)

# k = re.findall("[0-9]",st)

# k = re.findall(r"\D",st)

# k = re.findall(r"\Bcat\B","cat in ttrcatalog")

# print(k)

# k = re.findall(r"\d",st)
# k = re.findall(r"\D",st)
# k = re.findall(r"\w",st)
# k = re.findall(r"\W",st)
# k = re.findall(r"\d",st)
# k = re.findall(r"\s",st)
# k = re.findall(r"\S",st)
# k = re.findall(r"\bcat\b","cat in ttrcatalog")
# k = re.findall(r"\B","cat in ttrcatalog")
# k = re.findall(r"\n",st)
# print(k)

# phone = "9978997204"
# k re.match(r"^\d{10}$",phone)
# if k is None:
#     print("Invalid Phone Number!")
# else:
#     print("Valid Phone Number")

# email = "purva@gmail.com"
# k = re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]{2,4}$",email)
# print(k)      


username = "Purva"
k = re.match(r"^\D{3,10}$",username)
print(k)