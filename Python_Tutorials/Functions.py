#Learning how to call functions
"""
-A function is a block of code which only runs when it is called.
-You can pass data, known as parameters, into a function.
-A function can return data as a result.
"""



def my_function():
    print("hello")

#To call a function, use the function name followed by parenthesis:
my_function()


#Passing Arguments to a Function and calling it 
def names(fname):
    print(fname + " HI")

names("david")
names("robot")


#Passing 2 Arguments to a Function and calling it 
def cars(car,color):
    print(car, "" ,color)

cars("Benz","Red")