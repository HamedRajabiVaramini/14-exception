 # type: ignore
'''
simple_programming_

This code uses try, except and else block to 
test a piece of code for errors
''' 
x = 1
try:
    print(x) # raises no exception
except NameError:
    print("Variable 'x' is not defined")
else:
    print("Nothing went wrong")

