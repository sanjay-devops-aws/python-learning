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


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

# print my_list[::-1]


sample_url = 'http://coreyms.com'
print (sample_url)

# Reverse the url
print (sample_url[::-1])

# # Get the top level domain
print (sample_url[-4:])   

# # Print the url without the http://
print (sample_url[7:])

# # Print the url without the http:// or the top level domain
print (sample_url[7:-4])