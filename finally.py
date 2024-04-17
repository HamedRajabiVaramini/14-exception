 # type: ignore
'''
simple_programming_

This code uses try, except, finally block to 
test a piece of code for errors
''' 
try:
    print(x) # raises no exception
except NameError:
    print("Variable 'x' is not defined")
finally:
    print("We are done with testing.")

