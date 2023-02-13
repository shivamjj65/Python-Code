# 1. swap 2 numbers
def swap():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    (a,b) = (b,a)
    print("Num1 = ",a,"Num2 = ",b)

# 2. Find distance from origin
import math
def getDist():
    x = eval(input("Enter x co-ordinate"))
    y = eval(input("Enter y co-ordinate"))
    x1 = 0-x
    y1 = 0-y
    print("Distance from origin is: ",math.fabs(x1),math.fabs(y1))

print("---------------------------------------------------------")
userInput = int(input("Enter choice: 1.Swap 2.Find Distance from origin"))
if userInput==1:
    swap()
elif userInput==2:
    getDist()