# function calling itself
# fibonacci 0,1,1,2,3,5,8,13,...

def fibo(n):
    a = 0
    b = 1
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))



n = int(input("Enter nth term: "))
for i in range(0,n):
    print(fibo(i),end=" ")