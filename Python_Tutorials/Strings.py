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
print("")
b = "David Graham"
print(b +" IS THE STRING UNDER REVIEW")
bS = b[2:6] #ATTENTION
print("Sliced String from index 2 - index 5")
print(bS)
print("\n")

#Slice From Start To a Specific Index
print("PYTHON SLICING STRINGS FROM START TO A SPECIFIC INDEX.")
print("")
b = "David Graham"
print(b+" IS THE STRING UNDER REVIEW")
bS = b[:6] #ATTENTION
print("Sliced String from index 0 - index 5")
print(bS)
print("\n")

#Slice From A Specific Index to the END of a Particular string
print("PYTHON SLICING STRINGS FROM A SPECIFIC INDEX TO THE END OF A STRING.")
print("")
b = "David Graham"
print(b+" IS THE STRING UNDER REVIEW")
bS = b[6:] #ATTENTION
print("Sliced String from index 0 - index 5")
print(bS)
print("\n")

# NEGATIVE INDEXING 
# Use negative indexes to start the slice from the end of the string to the startof the string.
print("PYTHON SLICING STRINGS FROM THE BACK OF THE STRING TO THE FRONT OF THAT STRING.")
print("")
b = "David Graham"
print(b+" IS THE STRING UNDER REVIEW")
bS = b[-6:] #ATTENTION
print("Sliced String from index -6 - index -1")
print(bS)
print("\n")

#PYTHON MODIFYING OF STRINGS.

print("Python Modifying of Strings - TO UPPERCASE")
Mo = "Hello Kwesi"
print(Mo +" is the String Under Review Here")
Uppercase = Mo.upper() #METHOD FOR CONVERTING TO UPPERCASE
print(Uppercase + " now in UPPERCASE")
print("")

#PYTHON MODIFYING OF STRINGS.
print("Python Modifying of Strings - TO lowercase")
Mo = "HELLO KWESI"
print(Mo +" is the String Under Review Here")
lowercase = Mo.lower() #METHOD FOR CONVERTING TO lowercase
print(lowercase + " now in lowercase")
print("")

#PYTHON MODYFYING OF STRINGS
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

print("Python Modifying of Strings - TO Remove WhiteSpaces")
Mo = "  HELLO KWESI" # The Gaps infront of the string are the white spaces.

print(Mo +" is the String Under Review Here")
stRip = Mo.strip() #METHOD FOR Removing WhiteSpaces
print(stRip + " without whiteSpaces")
print("")

#Replacing Letters in A string with another letter
#Method Used .replace()
print("Replacing Letters in A string with another letter")
Re = "Pie Chart"
print(Re +" is the String Under Review Here")
print("Replacing C with D ")
Re2 = Re.replace("C","D")
print(Re2)
print("")

#The split() method splits the string into substrings if it finds instances of the separator:



#Using The Format Method
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
Age =24 
text = "I am David and i am {}"
foString = text.format(Age)
print(foString)
# Another Way to use the Formatted String
print("")
Age =24 
height = 44
text = "I am David and i am {}  and my respective height is {}"
foString = text.format(Age , height)
print(foString)
print("") 

#You can use Index to specify 
print("Using Indexes to Specify where a Formatted String will go")

Age =24 
height = 44
text = "I am David and i am {0}  and my respective height is {1}"
foString = text.format(Age , height)
print(foString)
print("") 

