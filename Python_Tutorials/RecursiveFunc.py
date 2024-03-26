#Creating a recursive function with the factorial principle (!)

def factorial(n):
    if n < 0:   #error handling
        raise ValueError("Factorial is not defined for negative numbers")   
    elif n == 0:   #base case
        return 1
    else:
       return n * factorial(n-1)#recursive case


#Test the function or Calling of the function with a test case.
print(factorial(5))  




    
