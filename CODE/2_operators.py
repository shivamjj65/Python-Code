"""Operators are used to perform some operation between some values of any data types.
We have seven different types of Operators in Python and can perform any operation but are differentiated according to
their usage. Like when we add two numbers we use addition operators between those numbers which can be int, or float, or
can be of another data type."""

# ARITHMETIC OPERATORS
print("\nARITHMETIC OPERATORS")
a = eval(input("Enter number 1 : "))  # eval automatically sets datatype according to input
b = eval(input("Enter number 2 : "))
print("\nAddition operator + : a+b=", a + b)
print("Subtraction operator - : a-b=", a - b)
print("Multiplication operator * : a*b=", a * b)
print("Division operator / : a/b=", a / b)
print("Modulus operator % : a*b=", a % b)
print("Exponential operator ** : a**b=", a ** b)  # return Raise to
print("Floor Division operator // : a//b=", a // b)  # return quotient

# ASSIGNMENT OPERATORS
print("\nASSIGNMENT OPERATORS")
x = eval(input("\nEnter x: "))
print("x = ", x)
x += 5
print("x = x+5 ie; x+=5 ie; x = ", x)
x -= 5
print("x = x-5 ie; x-=5 ie; x = ", x)
x *= 5
print("x = x*5 ie; x*=5 ie; x = ", x)
x /= 5
print("x = x/5 ie; x/=5 ie; x = ", x)
x %= 5
print("x = x%5 ie; x%=5 ie; x = ", x)
x //= 5
print("x = x//5 ie; x//=5 ie; x = ", x)
x **= 5
print("x = x**5 ie; x**=5 ie; x = ", x)
'''x &= 5
print("x = x&5 ie; x&=5 ie; x = ", (x))
x |= 5
print("x = x|5 ie; x|=5 ie; x = ", x)
x ^= 5
print("x = x^5 ie; x^=5 ie; x = ", x)
x >>= 5
print("x = x>>5 ie; x>>=5 ie; x = ", x)
x <<= 5
print("x = x<<5 ie; x<<=5 ie; x = ", x)
'''
# COMPARISON OPERATORS
print("\nCOMPARISON OPERATORS")
print("They are: ==  !=  >  <  >=  <=")

# LOGICAL OPERATORS
print("\nLOGICAL OPERATORS")
print("They are:  and  or  not")

# IDENTITY OPERATORS
print("\nIDENTITY OPERATORS")
print("They are:  is    is not")

# BITWISE OPERATORS
print("\nBITWISE OPERATORS")
print("They are:  & (and)  | (or)  ~ (not)  ^ (xor)  << (left shift)  >> (right shift) ")

# MEMBERSHIP OPERATORS
print("\nMEMBERSHIP OPERATORS")
print("They are:  in   not in")
