# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.items())
# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 

# output:
# The value corresponding to the key name is Karan
# The value corresponding to the key age is 19
# The value corresponding to the key eligible is True


 # dictory method:
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

# ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1) 