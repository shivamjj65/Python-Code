print("String in python is non-mutable predefined object")
name = "Narendra"
print(name)
print("2nd character in string is: ",name[2])
print("Last character in string is: ",name[-1])
print("Length of string is: ",len(name))
new_name = name + ' Modi'
print(new_name)

#Slicing : Extracting string from index values
first_name = new_name[0:8]
print(first_name)
new_name[0] = 'n' # throws error, string or its char cant be changed