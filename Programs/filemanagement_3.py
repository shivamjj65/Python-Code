
import os

# reading file
file = open("tetx.txt","r")
print(file.read())

#printig file data using for loop

for x in file:
    print(x)

file.close()


# appending
f = open("tetx.txt","a")
f.write("\n\nWritenn using append")
f.close()


# reading
file = open("tetx.txt","r")
print(file.read())
file.close()


# writing
newfile = open("newfile.txt","w")


#deleting file
if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("file not found")