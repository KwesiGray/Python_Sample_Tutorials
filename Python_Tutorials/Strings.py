# All About Python Strings I know
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("PYTHON STRINGS")
print("\n")

#First String
String = "Hello Welcome"
print(String)
print("\n")

#Using 3 Double Quotes to Print Multiple Line Strings
a = """
Strings in python are surrounded by either single
quotation marks, or double quotation marks.
"""
print(a)
print("\n")

#Printing Chracters from a String using their Index.
print("Printing Chracters from a String using their Index.")

a = "Human Being"
print(a + " Is the String Under Review")

print("Printing From index 0-5 of the word HUMAN BEING ")
print("The New String is: "+ a[0:5])

#Printing A Particular Text in a set of a strings
print("\n")
txt= "There's no free lunch in the world"
print(txt)
print("free" in txt)
#Returns "True" Because the word "Free" actually exists in the Sentence above.
print("\n")


#Using the same technique.But This time with a "IF Statement".
txt1 = "There's no free lunch in the world"
print(txt1)
print("Checking if the word Free is in the above String")
if "free" in txt1:
    print("Yes the Word Free is in the above string")
    x="Free"
    print(x)

print("\n")
#Check If Not 
txt3 = "Life is Expensive"
print(txt3)
print("Checking if the word Expensive is not in the above String")
print("Expensive" not in txt3)
print("\n")



#PYTHON SLICING STRINGS
print("PYTHON SLICING STRINGS")
