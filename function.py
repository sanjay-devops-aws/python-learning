
# Python function is a block of code, that runs only when it is called. It is programmed to return the specific task. 
# You can pass values in functions called parameters. It helps in performing repetitive tasks.

# The main types of functions in Python are:

# Built-in function
# User-defined function
# Lambda functions
# Recursive functions

# def calculateGmean(a, b):
#   mean = (a*b)/(a+b)
#   print(mean)

# def isGreater(a, b):
#   if(a>b):
#     print("First number is greater")
#   else:
#     print("Second number is greater or equal")

# def isLesser(a, b):
#   pass # Just pass agrument
  

# a = 9
# b = 8
# isGreater(a, b)
# calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
# c = 8
# d = 74
# isGreater(c, d)
# calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)

# output:
# First number is greater
# 4.235294117647059
# 4.235294117647059
# Second number is greater or equal
# 7.219512195121951
# 7.219512195121951

###

# def hello_func():
#     print("Hello Function!")

# hello_func()
# hello_func()
# hello_func()

# output:
# Hello Function!
# Hello Function!
# Hello Function!

# def hello_func():
#     return 'Hello Function!'

# print(len('Test'))

# print(hello_func().upper())

# def hello_func(greeting):    # pass argument
#     return '{} Function.'.format(greeting)

# print(hello_func('Hi'))

# def hello_func(greeting, name='You'):    # pass argument
#     return '{}, {}'.format(greeting, name)

# print(hello_func('Hi', name= 'Sanjay'))
# Output:
# 4
# HELLO FUNCTION!
# Hi Function.
# Hi, Sanjay

# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
	if (x % 2 == 0):
		print("even")
	else:
		print("odd")


# Driver code to call the function
evenOdd(2)
evenOdd(3)

### Argument pass
def average(a, b):
	print("The average is ", (a+b)/2)

average(4, 6)

# output:
# The average is  5.0

### keyword argument
def average(a=9, b=1):
	print("The average is ", (a+b)/2)

average(b=9, a=21)

### Required argument
def average(a, b, c=1):
	print("The average is ", (a+ b +c) / 2)

average(5, 6)

### variable lenght argument

def average(*numbers):
	print(type(numbers))
	sum =0
	for i in numbers:
		sum = sum + i
	print("Average is:", sum / len(numbers))

average(5, 6, 7, 1)

# output:
# <class 'tuple'>
# Average is: 4.75


# return statement
def average(*numbers):
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i

  return sum / len(numbers)

c = average(5, 6, 7, 1)
print(c)

# output:
# <class 'tuple'>
# 4.75