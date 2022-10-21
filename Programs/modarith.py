import math as m
def CONGRUENCE(div,d):
    print("THIS CAN BE WRITTEN AS:",div,"mod",d)
    q=div/d
    q1=int(q)
    if q1>0:
        q2=q1+1
    else:
        q2=q1-1
    print("\nQUOTIENT IS",q)
    print("SO Q1 AND Q2 WILL BE",q1,"and",q2)
    rem1=div-(d*q1)
    rem2=div-(d*q2)
    print("\nREMAINDER 1 IS:",rem1)
    print("REMAINDER 2 IS:",rem2)
    print(div,"=",d,"*",q1,"+",rem1)
    print(div,"=",d,"*",q2,"+",rem2)
    print("\nTHEREFORE IN CONGRUENCE FORM:")
    print(div,"=",rem1,"(mod",d,")")
    print(div,"=",rem2,"(mod",d,")")

print("----------------------------------------------------------------------------\n")
while True:
    print("\nENTER CHOICE")
    print("For simple sum PRESS 1")
    print("For power or raise to sums PRESS 2")
    x=eval(input())
    if x==1:
        div=eval(input("ENTER DIVIDEND\t"))
        d=eval(input("ENTER DIVISOR\t"))
        CONGRUENCE(div,d)
    elif x==2:
        print("ENTER IN FORM: a raise to b = mod d")
        print("\n WHERE a,b would be dividend and d will be divisor")
        a=eval(input("ENTER a"))
        b=eval(
            input("ENTER b"))
        div=m.pow(a,b)
        d=eval(input("ENTER DIVISOR\t"))
        CONGRUENCE(div,d)
    else:
        print("INVALID INPUT")
    
