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

def hello_func():
    return 'Hello Function!'

print(len('Test'))

print(hello_func().upper())

def hello_func(greeting):    # pass argument
    return '{} Function.'.format(greeting)

print(hello_func('Hi'))

def hello_func(greeting, name='You'):    # pass argument
    return '{}, {}'.format(greeting, name)

print(hello_func('Hi', name= 'Sanjay'))
# Output:
# 4
# HELLO FUNCTION!
# Hi Function.
# Hi, Sanjay

