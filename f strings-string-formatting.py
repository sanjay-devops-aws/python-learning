# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# val = 'Geeks'  
# print(f"{val}for{val} is a portal for {val}.")  
# name = 'Tushar'  
# age = 23  
# print(f"Hello, My name is {name} and I'm {age} years old.")

# print(f"{2 * 30}")

# Output:
# For only 49.00 dollars!
# GeeksforGeeks is a portal for Geeks.
# Hello, My name is Tushar and I'm 23 years old.   
# 60

###
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Harry"

print(letter.format(country, name))
print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}")
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
print(txt.format())
print(type(f"{2 * 30}"))