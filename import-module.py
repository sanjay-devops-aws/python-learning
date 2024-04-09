# import random

# courses = ['History', 'Math', 'physics', 'CompSci']

# random_course = random.choice(courses)

# print(random_course)

###

# import datetime
# import calendar

# today = datetime.date.today()

# print(today)
# print(calendar.isleap(2024))

# output:
# 2024-03-29
# True

###

# import os 

# print(os.getcwd()) # current working directory

# # output:
# # C:\Users\Sanjay\Documents\python-learning

# print(os.__file__)
 
# output:
# C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.7_3.7.2544.0_x64__qbz5n2kfra8p0\lib\os.py

# import antigravity 

# output:
# https://xkcd.com/353/

### this file import module other file 'my_module.py'
import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

# output:
# Imported my_module...


###

# from math import sqrt, pi
# from math import pi, sqrt as s
# import math as math_builtin_python

# result = math_builtin_python.sqrt(9) * math_builtin_python.pi
# print(result)  # Output: 3.0

# from harry import welcome, harry
# import harry as hr
# import math

# print(dir(math))
# print(math.nan, type(math.nan))
# hr.welcome()
# print(hr.harry)