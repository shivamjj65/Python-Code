print("\nSTRINGS IN PYTHON")
print("String data-type in Python programming language is used to store the string values in a variable. "
      "\nThe string is the only data type in python which can be used as a character similar like in Java and C."
      "\nIn python characters are also treated as a string and are referred to as a string of length 1. "
      "\nThe string is an immutable data type in python means we can’t append or remove item or element from the string"
      " variable")
print("\nEXAMPLE")
s = str(input("Enter string : "))
print("The string is : ", s)
print("s[0] is : ", s[0])  # prints 0th element of string
length = len(s)
print("length of string is: ", length)  # prints string length
for i in s:
    print("", i)  # iterating in string

print("\nCharacters in string from 4th to end are : ", s[3:length])
print("Reverse of string is : ", s[::-1])

# some functions
char = str(input("Enter to find character count in string: "))
print("Count of character ", char, " in string: ", s.count(char))
print("String to uppercase is: ", s.upper())
print("String to lowercase is: ", s.lower())
