"""
6. Matching a String Against a Regular Expression With matches()

"""
import re
line="pet:cat I love cats"
mat=re.match(r"pet:\w\w\w",line)
print(mat)