s = set()
print(type(s))  # <class 'set'>
s_from_list= set([1, 2, 3, 4])
print(s_from_list)  # {1, 2, 3, 4}
print(type(s_from_list)) # <class 'set'>

# 
s = set()
l = set([1, 2, 3, 4])
s_from_list = set(l)
print(s_from_list) 
print(type(s_from_list))

# Set find the unique value
s = set()
s.add(1) # {1}
s.add(1) # {1} same value not changed
s.add(2) # {1, 2}
print(s) # 

# 
s = set()
s.add(1)
s.add(2)
s1 = s.union({1, 2}) # {1, 2}
s1 = s.intersection({1, 2, 3})
print(s, s1)

#
s = set()
s.add(1)
s.add(2)
s1 = {4, 6}
print(s.isdisjoint(s1)) # True

# 
s = set()
s.add(1)
s.add(2)
s.remove(2) # {1}
s1 = {4, 6}
print(s)




