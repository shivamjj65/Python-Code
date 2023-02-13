print("Main 5 data-types in Python are : \n\t 1.Numeric 2.Dictionary 3.Boolean 4.Set 5.Sequence type")
print("1.Numeric : >> Integer >> Float >> Complex No")
print("5. Sequence Type : >> String >> List >> Tuple")



print("\n\n ----------------Numeric------------------")

'''Integer data types are the one which can hold the integral value of the number. 
Integer data-types are the most common data types used in every programming language to deal with the operations 
performed on integer values. When we use loop statements to iterate through some list or any other data type, 
we use the integer values to get the indexes of the element.'''

# user input of integer value
var1 = int(input("Enter a integer no: "))
c = var1 / 2  # c will store float
print("c = a / 2 = ", int(c))  # typecasted c

'''Float Data-types is one which holds the decimal values written after an integral part of the number along with an 
integral part. Float data-type is used to store accurate values. They can be used defined inputs or obtained by 
performing some operations. Float data-types can store values up to some exact digits and also can be formatted 
according to users need.'''

# user input of float value
var2 = float(input('Enter the float value :'))
print(var2)

'''Complex numbers are the data-type category that stores the complex numbers in a variable. Complex numbers are a
combination of two different parts, one is a real part and another is the imaginary part. Complex numbers are 
written as Complex_number = 5+89j. Complex numbers are used to solve advance calculus problems.'''

# user input of complex value
var3 = complex(input('Enter the complex number ie; x + yj :'))
print(var3)





'''Dictionaries in the Python Programming languages is the set of key holding some value to it and can be of any 
data-type. Dictionaries are created by placing the sequence of element inside the curly brackets {}, 
separated by commas. Values are the data stored in the key and can be duplicated, but keys are unique and duplicating 
keys are not allowed.'''
print("\n\n ------------------Dictionary------------------\n")
# creating dictionary
dictionary = dict({'Name': 'Shivam', 'Contact': 8080801, 'Id': 'Xy123'})
# printing dictionary
print(dictionary)
print(dictionary.keys())
print(dictionary.values())




'''Boolean data-type is used to store values with True and False. True value is stored the 1 and False stores the 0.'''
print("\n\nBoolean")
check = bool(input("\nType True of False : "))
if check:
    print("You Entered True")
else:
    print("You Entered False")






'''Sets are Data-type like the list. In this type of data type, we can store different values which are non-repeating. 
Sets remove the duplicates of the elements and rearrange them in an unpredictable arrangement. We cannot define the 
position of the element in the set but sets help find if the element is available in it or not.'''
print("\n\nSets\n")
Set = set([1,2,3,4,3,1,6])
print(Set)
#check for element
if 1 in Set:
    print('Present')





'''The sequence in a python programming language is a collection of data of same data-type or different data-type. 
In sequences, we can store items or elements and can efficiently perform operations.'''

# LIST  is mutable ie; can be changed
print("\n\nList")
List = [1,2,3,4,5]
for i in range(0,4):
    print(List[i])
print(type(List))

# String
print("\n\nString")
wish = "Have a good day !"
name = str(input("Enter name: "))
print(wish,"",name)
print(type(wish))

# Tuple is immutable ie; data cant be changed, to change we need to create copy
print("\n\nTuple")
#initializing a tuple
Tuple = tuple([1,2,3,1,2])
print(Tuple)
#Printing type of sequence
print(type(Tuple))