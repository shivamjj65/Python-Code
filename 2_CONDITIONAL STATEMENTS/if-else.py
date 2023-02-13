num = int(input("Enter num: "))

if(num%2==0):
    print("Num is even")
else:
    print("Num is odd")

# ternary
result = ("even" if(num%2==0) else "odd")
print(result)

