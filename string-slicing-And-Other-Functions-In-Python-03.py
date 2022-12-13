mystr = "Harry is a good boy"
print(mystr[4])

#
print(mystr[0:4])
print(len(mystr))  # 19
print(mystr[0:19])
print(mystr[0:5:2])
""" Hry """

print(mystr[0:19:1])  # Harry is a good boy
print(mystr[::])
"""Harry is a good boy"""

print(mystr[::2])  # Hryi  odby

#
print(mystr[-1:])   # y
print(mystr[-4:])   # boy
print(mystr[-4:-2]) # b

# string intercahnge
print(mystr[::-1])  # yob doog a si yrraH
print(mystr[::-2])  # ybdo  iyrH

# String Functions
mystr = "Harry is a good boy"
print(mystr.endswith("boy")) # True
print(mystr.endswith("bdoy")) # False

print(mystr.count("o")) # 3 

print(mystr.capitalize()) # H capital 

print(mystr.replace("is", "are")) # Harry are a good boy

print(mystr.find("is")) # 6

print(mystr.upper()) # HARRY IS A GOOD BOY
print(mystr.lower()) # harry is a good boy


