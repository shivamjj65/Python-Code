# *
# **
# ***
n1 = int(input("Enter no of lines: "))
for i in range(1,n1+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")


# 1
# 22
# 333
for i in range(1,n1+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")


# 1
# 12
# 123
# 1234
for i in range(1,n1+1):
    for j in range(0,i):
        print(j+1,end=" ")
    print("\n")


# 1
# 23
# 456
k=1
for i in range(1,n1+1):
    for j in range(0,i):
        print(k,end=" ")
        k=k+1
    print("\n")


#   *
#  ***
# *****
