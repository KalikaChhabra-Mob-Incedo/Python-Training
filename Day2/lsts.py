# Python program to demonstrate  
# Creation of List  
  
# Creating a List 
List = [] 
print("Intial blank List: ") 
print(List) 
  
# Creating a List with  
# the use of a String 
List = ['GeeksForGeeks'] 
print("\nList with the use of String: ") 
print(List) 
  
# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 
print("\nList containing multiple values: ") 
print(List[0])  
print(List[2]) 
  
# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List = [['Geeks', 'For'] , ['Geeks']] 
print("\nMulti-Dimensional List: ") 
print(List) 
  
# Creating a List with  
# the use of Numbers 
# (Having duplicate values) 
List = [1, 2, 4, 4, 3, 3, 3, 6, 5] 
print("\nList with the use of Numbers: ") 
print(List) 
  
# Creating a List with  
# mixed type of values 
# (Having numbers and strings) 
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks'] 
print("\nList with the use of Mixed Values: ") 
print(List)


# Python program to demonstrate  
# Addition of elements in a List 
  
# Creating a List 
List = [] 
print("Intial blank List: ") 
print(List) 
  
# Addition of Elements  
# in the List 
List.append(1) 
List.append(2) 
List.append(4) 
print("\nList after Addition of Three elements: ") 
print(List) 
  
# Adding elements to the List 
# using Iterator 
for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 
  
# Adding Tuples to the List 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 
  
# Addition of List to a List 
List2 = ['For', 'Geeks'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 
  
# Addition of Element at  
# specific Position 
# (using Insert Method) 
List.insert(3, 12) 
List2.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 
  
# Addition of multiple elements 
# to the List at the end 
# (using Extend Method) 
List.extend([8, 'Geeks', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List) 


# Python program to demonstrate 
# Removal of elements in a List 

# Creating a List 
List = [1, 2, 3, 4, 5, 6, 
		7, 8, 9, 10, 11, 12] 
print("Intial List: ") 
print(List) 

# Removing elements from List 
# using Remove() method 
List.remove(5) 
List.remove(6) 
print("\nList after Removal of two elements: ") 
print(List) 

# Removing elements from List 
# using iterator method 
for i in range(1, 5): 
	List.remove(i) 
print("\nList after Removing a range of elements: ") 
print(List) 

# Removing element from the 
# Set using the pop() method 
List.pop() 
print("\nList after popping an element: ") 
print(List) 

# Removing element at a 
# specific location from the 
# Set using the pop() method 
List.pop(2) 
print("\nList after popping a specific element: ") 
print(List) 



# Python program to demonstrate 
# Removal of elements in a List 

# Creating a List 
List = ['G','E','E','K','S','F', 
		'O','R','G','E','E','K','S'] 
print("Intial List: ") 
print(List) 

# Print elements of a range 
# using Slice operation 
Sliced_List = List[3:8] 
print("\nSlicing elements in a range 3-8: ") 
print(Sliced_List) 

# Print elements from beginning 
# to a pre-defined point using Slice 
Sliced_List = List[:-6] 



# Python code to demonstrate the working of 
# del and pop() 

# initializing list 
lis = [2, 1, 3, 5, 4, 3, 8] 

# using del to delete elements from pos. 2 to 5 
# deletes 3,5,4 
del lis[2 : 5] 

# displaying list after deleting 
print ("List elements after deleting are : ",end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 

print("\r") 


# Python code to demonstrate the working of 
# insert() and remove() 

# initializing list 
lis = [2, 1, 3, 5, 3, 8] 

# using insert() to insert 4 at 3rd pos 
lis.insert(3, 4) 

# displaying list after inserting 
print("List elements after inserting 4 are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using remove() to remove first occurrence of 3 
# removes 3 at pos 2 
lis.remove(3) 

# displaying list after removing 
print ("List elements after removing are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 

# using pop() to delete element at pos 2 
# deletes 3 
lis.pop(2) 

# displaying list after popping 
print ("List elements after popping are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 

print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 

# Print elements from a 
# pre-defined point to end 
Sliced_List = List[5:] 
print("\nElements sliced from 5th "
	"element till the end: ") 
print(Sliced_List) 

# Printing elements from 
# beginning till end 
Sliced_List = List[:] 
print("\nPrinting all elements using slice operation: ") 
print(Sliced_List) 

# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) 


# Python code to demonstrate the working of 
# sort() and reverse() 

# initializing list 
lis = [2, 1, 3, 5, 3, 8] 

# using sort() to sort the list 
lis.sort() 

# displaying list after sorting 
print ("List elements after sorting are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 
	
print("\r") 

# using reverse() to reverse the list 
lis.reverse() 

# displaying list after reversing 
print ("List elements after reversing are : ", end="") 
for i in range(0, len(lis)): 
	print(lis[i], end=" ") 

  
 # Python code to demonstrate the working of 
# extend() and clear() 

# initializing list 1 
lis1 = [2, 1, 3, 5] 

# initializing list 1 
lis2 = [6, 4, 3] 

# using extend() to add elements of lis2 in lis1 
lis1.extend(lis2) 

# displaying list after sorting 
print ("List elements after extending are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
	
print ("\r") 

# using clear() to delete all lis1 contents 
lis1.clear() 

# displaying list after clearing 
print ("List elements after clearing are : ", end="") 
for i in range(0, len(lis1)): 
	print(lis1[i], end=" ") 
