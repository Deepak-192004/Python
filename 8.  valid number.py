import re
def is_valid_number(s):
    pattern = r"^[+-]?(\d+\.?\d*|\.\d+)?$"
    match = re.search(pattern,s)
    return bool(match)
print(is_valid_number("0"))
print(is_valid_number("e"))
print(is_valid_number(" "))
print(is_valid_number("."))
print(is_valid_number("%"))
