def findgcd():
    a=eval(input("enter a"))
    b=eval(input("enter b"))
    q=0
    while b!=0:
        q=b
        b=a%b
        a=q
    print("gcd is",a)
    print("---------------------------")
i=eval(input("enter i"))
while i!=0:
    findgcd()
    

    

    
    
