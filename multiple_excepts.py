 # type: ignore
'''
simple_programming_

This code uses try block with multiple 
excepts to test a piece of code for errors
''' 
try:
    print(x) # raises NameError exception
    print(2/0) # raises ZeroDivisionError exception
except NameError:
    print("Variable 'x' is not defined")
except ZeroDivisionError:
    print("Division by zero exception")
except: # for other reasons
    print("Unknown issue happend")

