name = "narendra damodardas modi"
party = "Bhartiya Janata Party"

# len()
print("Length of name is: ",len(name))
print("Length of party is: ",len(party))

# capitalize()
print(name.capitalize())

# find()
print("Occurences of char 'P' in party is at location : ",party.find('P'))

# count()
print("Occurences of char 'a' in name is : ",name.count('a'))

# encode()
encoded_name  = name.encode(encoding='utf32',errors='strict')
print(encoded_name)