#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# WHILE LOOPS
# Set the name variable to empty to accept the input from the user
# Goal is to make the user stuck in a loop if his/her name is not entered

name = ""
while len(name) == 0:
   name = input("Enter Your Name!")
print ("Hello "+name)

#FOR LOOPS
#How to write a simple For Loop.
print("A simple For loop using the range function.")
for i in range(10):
    print(i+1)

#The Range function format(start,end,step size)
print("")
print("Implementing the range function format here")
for index in range(50,100+1,5):
   print(str(index) +str(" shy"))

print("")

#Printing Every Letter in a String
print("Printing or iterating through a string using the for loop")
for i in "David Graham":
    print("The letters of the string are")
    print(i)
    
print("")
 
#Using the time Import.

import time

# importing time and using it as a countdown timer

print("Printing the sentence happy new year after a countdown timer.")
for seconds in range(3,0,-1):
  print(seconds)
  time.sleep(1)
print ("Happy New Year!!!!!!")

print("")
      
#using a for loop to find the first 10 multiples of 2  
print("using a for loop to find the first 10 multiples of 2")     
for j in range(1,10+1,1):
  print(j*2)
  
#How to Iterate through an array with string items using a For Loop.

print("How to Iterate through an array with string items using a For Loop.")
Fruits =["Grapes,Cherry,Orange,Kiwi,Apple"]
for f in Fruits:
  print(f)

#How to iterate through the letters of a given String
for q in  "Grapes": 
  print(q)
  
#Using the break statement involving a For Loop.

print("Using the break statement involving a For Loop")

names =["David","Salma","Thelma","Kwesi","Daniel"]
for n in names:
  print(n)
  if n == "Thelma":
    break
  
print("") 

#for this time around you print "r" after the break statement.
print("for this time around you print /r/ after the break statement")
for r in names:
    if r == "Kwesi":
     break
print("r is "+r)

print("")

#Using the Continue statement in a For Loop
print("Using the Continue statement in a For Loop")

Cars = ["Benz","Apollo","Ferrari","Dodge","Jeep"]

for c in Cars:
  print(c)
  if c == "Apollo":
    continue
print("")

#nested loops in python
print("nested loops in python")
  
  
adj =["bright","dim","dark","dirty"]
color2 =["yellow","white","red","ash"]

for c1 in adj:
  for c2 in color2:
    print(c1,c2)
print("results above..")
print("it prints the first array elements paired with the second array elements")
  
  
#Using the 'Pass' Statement in a For Loop to prevent an error in your code
#This Statement is generally used when for one reason you have an empty FOR LOOP BLOCK of code
print("")

print("Using the pass statement in a For loop to prevent errors.")
for x in [0,4,2,4]:
  pass

