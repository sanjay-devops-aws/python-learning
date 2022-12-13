# python list function
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",
           "Lollypop", 56]


print(grocery)

# 
print(grocery[1]) # vim bar

#
numbers = [2, 7, 9, 11, 3]
print(numbers[2]) # 9
numbers.sort()    # [2, 3, 7, 9, 11]
numbers.reverse() # [11, 9, 7, 3, 2]
print(numbers) 

#
numbers = [2, 7, 9, 11, 3]
print(numbers[:5]) # [2, 7, 9, 11, 3]
print(numbers[:])  # [2, 7, 9, 11, 3] default value
print(numbers[1:]) # [7, 9, 11, 3]
print(numbers[1:4]) # [7, 9, 11]
print(numbers[::1]) # [2, 7, 9, 11, 3]
print(numbers[::2]) # [2, 9, 3]

# 
print(numbers[::-3]) # [3, 7]
print(numbers[1:5:-3]) # [] Note:  Dont take any minux value more then -1 in string or list

# 
print(min(numbers))
print(max(numbers))
numbers.append(72)    # [2, 7, 9, 11, 3, 72]
print(numbers)

# 
numbers = []
numbers.append(2)
numbers.append(4)
numbers.append(6)
print(numbers)       # [2, 4, 6]


#
numbers = [2, 7, 9, 11, 3]
numbers.insert(3, 67)
print(numbers)

numbers = [2, 7, 9, 11, 3]
numbers.remove(9)
numbers.pop() # [2, 7, 9, 11]  # last number removed
print(numbers)

# 
numbers = [2, 7, 9, 11, 3]
numbers[1] = 98  # Add number 
print(numbers)  # [2, 98, 9, 11, 3]

# Mutable - can change
# Immutable - cannot change

# Ex. tp = (1, 2, 3)  # Mutable - can change
# tp[1] = 8
# print(tp) # error throwing value can not changed

tp = (1, 2, 3) # Immutable - cannot change
tp = (1) # 1
tp = (1,) # (1,)
print(tp)

#
a = 1
b = 8
a,b = b,a
print(a, b) # 8 1 

