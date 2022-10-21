#program on IF ELSE
a=eval(input("enter a"))
b=eval(input("enter b"))
c=eval(input("Enter choice: 1.ADD 2.SUB 3.MUL 4.DIV"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print("invalid input")
