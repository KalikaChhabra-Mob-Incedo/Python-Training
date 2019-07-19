# Try to guess the result before you actually run it 
import this 


# Multiple Return Values in Python! 
def func(): 
   return 1, 2, 3, 4, 5
  
one, two, three, four, five = func() 
  
print(one, two, three, four, five) 

# One can use an “else” clause with a “for” loop in Python.
# It’s a special type of syntax that executes only if the for loop exits naturally, without any break  statements.
def func(array): 
     for num in array: 
        if num%2==0: 
            print(num) 
            break # Case1: Break is called, so 'else' wouldn't be executed. 
     else: # Case 2: 'else' executed since break is not called 
        print("No call for Break. Else is executed")  
  
print("1st Case:") 
a = [2] 
func(a) 
print("2nd Case:") 
a = [1] 
func(a) 
