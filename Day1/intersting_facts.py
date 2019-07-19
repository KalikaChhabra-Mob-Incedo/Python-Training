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


# Well, python does not have pointers, but the objects are passed to functions by reference (and so in java, another language without pointers). 
# This mechanism is very similar to passing pointers by value in C.

# We call them references. They work like this

i = 5     # create int(5) instance, bind it to i
j = i     # bind j to the same int as i
j = 3     # create int(3) instance, bind it to j
print i   # i still bound to the int(5), j bound to the int(3)

#Small ints are interned, but that isn't important to this explanation

i = [1,2,3]   # create the list instance, and bind it to i
j = i         # bind j to the same list as i
i[0] = 5      # change the first item of i
print j       # j is still bound to the same list as i
