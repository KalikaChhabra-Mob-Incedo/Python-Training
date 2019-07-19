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


# Function Argument Unpacking is another awesome feature of Python.
# One can unpack a list or a dictionary as function arguments using * and ** respectively. 
# This is commonly known as the Splat operator.

def point(x, y): 
    print(x,y) 
  
foo_list = (3, 4) 
bar_dict = {'y': 3, 'x': 2} 
point(*foo_list) # Unpacking Lists 
point(**bar_dict) # Unpacking Dictionaries 

# Positive Infinity 
p_infinity = float('Inf') 
  
if 99999999999999 > p_infinity: 
    print("The number is greater than Infinity!") 
else: 
    print("Infinity is greatest") 
  
# Negetive Infinity 
n_infinity = float('-Inf') 
if -99999999999999 < n_infinity: 
    print("The number is lesser than Negative Infinity!") 
else: 
    print("Negative Infinity is least") 
      

# Slicing
a = [1,2,3,4,5] 
  
print(a[0:2]) # Choose elements [0-2), upper-bound noninclusive 
  
print(a[0:-1]) # Choose all but the last 
  
print(a[::-1]) # Reverse the list 
  
print(a[::2]) # Skip by 2 
  
print(a[::-2]) # Skip by -2 from the back 


# Strings are Immutable
# Once a string is defined, it cannot be changed.

# Python3 program to show that  
# string cannot be changed 
  
a = 'Geeks'
  
# output is displayed 
print(a) 
  
a[2] = 'E'
print(a) # causes error 

# Python3 program to show that  
# a string can be appended to a string. 
  
a = 'Vivek'
  
# output is displayed 
print(a) 
a = a + 'Srivastava'
  
print(a) # works fine 


# Python3 program to show that 
# both string hold same identity 
  
string1 = "Hello"
string2 = "Hello"
  
print(id(string1)) 
print(id(string2)) 


# Python program processing 
# global variable 
  
count = 5
def some_method(): 
    global count 
    count = count + 1
    print(count) 
some_method() 


#Declared using Continuation Character (\):
s = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

#Declared using parentheses () :
n = (1 * 2 * 3 + 7 + 8 + 9)

#Declared using square brackets [] :
footballer = ['MESSI',
          'NEYMAR',
          'SUAREZ']

#Declared using braces {} :
x = {1 + 2 + 3 + 4 + 5 + 6 +
     7 + 8 + 9}

#Declared using semicolons(;) :
flag = 2; ropes = 3; pole = 4

# Python program showing 
# indentation 
  
site = 'gfg'
  
if site == 'gfg': 
    print('Logging on to geeksforgeeks...') 
else: 
    print('retype the URL.') 
print('All set !') 


# This is a comment 
# Print “Vivek Srivastava !” to console 
print("Vivek Srivastava") 


""" 
This would be a multiline comment in Python that 
spans several lines and describes . 
"""
print("Vivek Srivastava") 


#Python code to demonstrate working of iskeyword() 

# importing "keyword" for keyword operations 
import keyword 

# initializing strings for testing 
s = "for"
s1 = "geeksforgeeks"
s2 = "elif"
s3 = "elseif"
s4 = "nikhil"
s5 = "assert"
s6 = "shambhavi"
s7 = "True"
s8 = "False"
s9 = "akshat"
s10 = "akash"
s11 = "break"
s12 = "ashty"
s13 = "lambda"
s14 = "suman"
s15 = "try"
s16 = "vaishnavi"

# checking which are keywords 
if keyword.iskeyword(s): 
		print ( s + " is a python keyword") 
else : print ( s + " is not a python keyword") 

if keyword.iskeyword(s1): 
		print ( s1 + " is a python keyword") 
else : print ( s1 + " is not a python keyword") 

if keyword.iskeyword(s2): 
		print ( s2 + " is a python keyword") 
else : print ( s2 + " is not a python keyword") 

if keyword.iskeyword(s3): 
		print ( s3 + " is a python keyword") 
else : print ( s3 + " is not a python keyword") 

if keyword.iskeyword(s4): 
		print ( s4 + " is a python keyword") 
else : print ( s4 + " is not a python keyword") 

if keyword.iskeyword(s5): 
		print ( s5 + " is a python keyword") 
else : print ( s5 + " is not a python keyword") 

if keyword.iskeyword(s6): 
		print ( s6 + " is a python keyword") 
else : print ( s6 + " is not a python keyword") 

if keyword.iskeyword(s7): 
		print ( s7 + " is a python keyword") 
else : print ( s7 + " is not a python keyword") 

if keyword.iskeyword(s8): 
		print ( s8 + " is a python keyword") 
else : print ( s8 + " is not a python keyword") 

if keyword.iskeyword(s9): 
		print ( s9 + " is a python keyword") 
else : print ( s9 + " is not a python keyword") 

if keyword.iskeyword(s10): 
		print ( s10 + " is a python keyword") 
else : print ( s10 + " is not a python keyword") 

if keyword.iskeyword(s11): 
		print ( s11 + " is a python keyword") 
else : print ( s11 + " is not a python keyword") 

if keyword.iskeyword(s12): 
		print ( s12 + " is a python keyword") 
else : print ( s12 + " is not a python keyword") 

if keyword.iskeyword(s13): 
		print ( s13 + " is a python keyword") 
else : print ( s13 + " is not a python keyword") 

if keyword.iskeyword(s14): 
		print ( s14 + " is a python keyword") 
else : print ( s14 + " is not a python keyword") 

if keyword.iskeyword(s15): 
		print ( s15 + " is a python keyword") 
else : print ( s15 + " is not a python keyword") 

if keyword.iskeyword(s16): 
		print ( s16 + " is a python keyword") 
else : print ( s16 + " is not a python keyword")
   

# Python 2 code for printing 
# on the same line printing 
# geeks and geeksforgeeks 
# in the same line 

print("geeks"), 
print("geeksforgeeks") 

# array 
a = [1, 2, 3, 4] 

# printing a element in same 
# line 
for i in range(4): 
	print(a[i]), 

# Python 3 code for printing 
# on the same line printing  
# geeks and geeksforgeeks  
# in the same line 
  
print("geeks", end =" ") 
print("geeksforgeeks") 
  
# array 
a = [1, 2, 3, 4] 
  
# printing a element in same 
# line 
for i in range(4): 
    print(a[i], end =" ") 
