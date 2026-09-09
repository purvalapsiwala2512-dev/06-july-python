import re

def is_valid_pnr(x):

    if re.match(r"^\d{10}$",x):
        return True
    else:
        return False

print(is_valid_pnr("7878795960"))   
print(is_valid_pnr("12345"))     
print(is_valid_pnr("012345xyzw"))