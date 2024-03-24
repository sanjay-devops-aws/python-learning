# Ex-01

#var1 = 6
#var2 = 56

#var3 = int(input())

#if var3>var2:
#    print("Greater")
#elif var3==var2:
#    print("Equal")

#else:
#    print("Lesser")

# Ex-02
 
list1 = [5, 7, 3]
print(5 in list1)  # True
if 5 in list1:
    print("Yes its in the list")

# Ex-03

list1 = [5, 7, 3]
print(15 not in list1)  # True
if 15 not in list1:
    print("No its not in the list")

# Ex-04
print("What is your age?")
age = int(input())             # User Input
if age<18:
    print("You cannot drive")

elif age==18:
    print("We will think about you")

else:
    print("You can drive")

# if condition
    
a = int(input("Enter your age: "))
print("Your age is:", a)
# Conditional operators 
# >, <, >=, <=, ==, !=
# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)
if(a>18):
  print("You can drive")
  print("Yes")
else:
  print("You cannot drive")
  print("No")
  print("Yay!")


# Ex if else condition

applePrice = 10
budget = 200
if (budget - applePrice > 50):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")


# Ex elif
    
num = int(input("Enter the value of num: "))
if (num < 0):
  print("Number is negative.")
elif (num == 0):
  print("Number is Zero.")
elif (num == 999):
  print("Number is Special.")
else:
  print("Number is positive.")

print("I am happy now")

# Ex Nested condition

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
