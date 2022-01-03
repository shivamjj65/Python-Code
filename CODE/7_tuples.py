'''Tuples :
Creating tuples in python is faster than creating a list in python.
For competitive coding, wherever we need a list we can use a tuple if there is no need for modification of an element in the list.
It consumes less memory than a list.
We can not delete an element from the tuple but we have some hacks to perform this operation.
We can edit or change any element of the tuple.
If we try to modify an element of the tuple, we will get a compilation error.
Sometime python get TLE, in that case, we can use a tuple instead of a list.
'''

# creating a tuple
a=()
print(a)
a = (1,2,'3')
print(a)

#opertion on tuple
a = ('s','h','i')
b = ('v','a','m')
c=(a+b)
print(c)

# finding maximum and min element from tuple
a  =  (1,2,3,3,4,5,6,7,7,56,5)
print(a)
print("Max in a is: ",max(a))
print("Min in a is: ",min(a))
print("Length of a is: ",len(a))

# convert tuple -> list
x = list(a)
print(x)