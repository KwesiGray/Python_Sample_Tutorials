import random

#Using the Random Import.

jay = random.randrange(1,10)
print(str(jay)+ " is the random number printed from 1 to 9 with 10 exclucive")


g= 3+5j + 4+3j
print(g)

print("")

# How to print Paragraphs in Python or A MultiLine Comment
print("How to print Paragraphs in Python or A MultiLine Comment in Python.")
print("")

Par='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''
print(Par)

#Printing Chracters from a String using their Index.
print("")
print("Printing Chracters from a String using their Index.")

a = "Human Being"
print(a + " Is the String Under Review")

print("Printing From index 0-5 of the word HUMAN BEING ")
print("The New String is: "+ a[0:5])
print("\n")

x = "Hello World"
print("The String Under Review is: "+ x)
print("Printing the 3rd index of the above string")
print("\n")
a = x[3]
print("The Third Index of the Above String is: "+ a)
