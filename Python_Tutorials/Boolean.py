# BOOLEANS
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.

# A Simple Boolean Representation 
print(10 > 9) #Prints True 
print(10 == 9) # Prints False
print(10 < 9) # Prints False
print("\n")

# Print a message based on whether the condition is True or False:

print("Using the IF STATEMENTS HERE to check whether a condition is true or not")

a = 34
b = 13.5
print("A is " + str(a))
print("B is " + str(b))

if a>b :
    print("A is greater than b")
else:
    print("B is greater or equal to a")
print("\n")

#Evaluate Variables and variables  
# Using the bool Fuction
# The bool() function allows you to evaluate any value, and give you True or False in return
print("A Simple Illustration with the bool function")
print(bool("hello"))  
print(bool(89))
print("\n")

"""Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
 """
 
#Functions can also be in this case a Boolean.
print("Making A function a Boolean.")
print("Creating for the boolean TRUE..")
def myTrueBool():
    return True
print(myTrueBool())
print("\n")


print("Creating for the boolean FALSE..")
def myFalseBool():
    return False
print(myFalseBool())
print("\n")

#You can execute code based on the Boolean answer of a function:
# A Code to Print "YES!" if the function returns True, otherwise print "NO!":

print("A Code to Print YES! if the function returns True, otherwise print NO!")
def myFunction():
    return True

if myFunction:
    print("YESSS!!!")
else:
    print("NO!")
    
print("\n")