print(">> Files are accessed using file objects. \n>>There are 3 steps.\n open(), Operate on files, close()")
print("Files are opened using open() function with different modes ie; read, write, append")

# different parameters go into open() as modes, r-read, w-write, a-append, etc

# open file in read mode
f = open('demoFile.txt','r')
print("Name of file is: ",f.name)
print("Mode of file is: ",f.mode)
print("\nFirst line of file is: ",f.readline())
print("Data in file is: ",f.readlines())
print("\nIs file closed? ",f.closed)
f.close()
print("Is file closed? ",f.closed)


# open file in write mode
f = open('demoFile.txt','w')
f.write("Hello, How are you?\nI am fine")
f.close()

# rename file os.rename('original_name','new_name')
import os
os.rename('demoFile.txt','demoFile.txt')