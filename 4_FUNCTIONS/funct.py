'''The function is a block of related statements that performs a specific task when it is called.
Functions helps in breaking our program into smaller and modular chunks which makes our program more organized and
manageable. Also, it avoids repetition and makes the code reusable.'''
import  math
print("Python has 2 types of functions ie;\n1.BUILT IN\n2.USER DEFINED")

# BUILT IN
x = 7
print("power of 7 raise to 2 is: ",pow(7,2))

# USER DEFINED
def calc(a,b):
    print(a + b)
    print(a - b)
    print(a / b)
    print(a * b)

a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
calc(a,b)