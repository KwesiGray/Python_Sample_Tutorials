# IF Statements = A block of code that will execute only if its condition is true
print("Implementing IF-Statements in a Simple Way")
print("\n")
age = int(input("How old are you?"))

if age >= 18:
    print("You are an adult")
elif age <=12:
    print("You are not a Teenager!")
elif age < 0:
    print("You haven't been born Yet!")
else:
    print("You are young")
