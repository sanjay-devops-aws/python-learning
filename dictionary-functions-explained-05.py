# Dictionary is nothing but key value pairs
d1 = {}
print(type(d1)) # <class 'dict'>

d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}

print(d2)

print(d2["Harry"]) # Burger
print(d2["Rohan"]) # Fish  

print(d2["Shubham"]) # {'B': 'maggie', 'L': 'roti', 'D': 'Chicken'}
d2["Ankit"] = "Junk Food"
d2["420"] = "Kababs"
del d2["420"] # deleted 
print(d2)

# 
# d3 = d2   # removed Harry
# del d3["Harry"]
# print(d2)

d3 = d2.copy()  # shallow copy
del d3["Harry"]
print(d2)
print(d2.get("Harry")) # Burger
d2.update({"Leena":"Toffee"}) # Added 
print(d2)
print(d2.keys()) # All keys Print
print(d2.items())

