def pm():
    print("**************************************************************************")
    print("\nCHECK FOR PRIME NUMBER")
while True:
    pm()
    lower=eval(input("ENTER LOWER LIMIT:"))
    upper=eval(input("ENTER UPPER LIMIT:"))
    print("---------------------------------------------")
    print("---------------------------------------------")
    print("Prime numbers between", lower, "and", upper, "are:")
    for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
       if num>1 :
           for i in range(2,num):
               if (num % i) == 0:
                  break
           else:
                print(" ",num)
    print("----------------------------------------------")
    print("----------------------------------------------")
    num=upper
    if num > 1:
   # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"is not a prime number")
               print(i,"times",num//i,"is",num)
               break
       else:
           print(num,"is a prime number")
# if input number is less than
# or equal to 1, it is not prime
    else:
       print(num,"is not a prime number")

