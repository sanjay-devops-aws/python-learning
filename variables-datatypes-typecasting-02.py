var1 = "hello world"
print(var1)

# check class type

var1 = "hello world"
var2 = 4
var3 = 36.5
print(type(var3))

"""
output
<class 'str'>
<class 'int'>
<class 'float'>
"""

# 

var1 = "hello world "   # space then doble quatation 
var2 = 4
var3 = 36.5
var4 = "Sanjay"
print(var2 + var3)

"""
output
40.5
"""
print(var1 + var4)

# concatination

var1 = "54 "
var2 = "32"
print(var1 + var2)

"""
output
54 32
"""
print(int(var1) + int(var2))
"""
output
86
"""

# 
print(10 * "Hello world")
print(10 * "Hello world\n")

#
print(100 * str(int(var1) + int(var2)) )

# user input
print("Enter your Number")
inpnum = input()              # Default take str
print("You entered ", inpnum)

"""
Enter your Number
112
You entered  112
"""
#
print("You entered ", int(inpnum)+10)
"""
You entered  22
"""

# calculator create
print("Enter first number")
n1= input()
print("Enter second number")
n2=input()
print("sum of these two numbers is", int(n1) + int(2))

"""
Enter first number
2
Enter second number
2
sum of these number is 4
"""

