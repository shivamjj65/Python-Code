print("\nLOOPS")
print("In programming loops are structure that repeats a sequence of instruction until a specific condition is met")
print("Types:\n\tFOR LOOP\n\tWHILE LOOP\n")
print("SYNTAX FOR LOOP:\n")
print("for iterator_variable in range/sequence : \n\t//statements")
print("SYNTAX WHILE LOOP:\n")
print("while(condition):\n\t//statements")
print("Example: ")

i = 0
for i in range(0, 5):
    print("Hello World !")

x = 0
while x <= 5:
    print("x =", x)
    x = x + 1

print("\n-------CONTINUE AND BREAK-------")
print("CONTINUE\nIt is a loop control statement.It forces the loop to execute the next iteration of the loop.")
print("SYNTAX:\nLoop from 1 to n :\n\tif (condition ): #True\n\t\tContinue")
print("else :\n\tremaining body of the loop  ")
print(
    "BREAK\nIt is a loop control statement.Break statement is used to terminate the loop , "
    "if a specific condition arises.")
print("SYNTAX:\nLoop from 1 to n\n\tif( condition ) : #true\n\t\tbreak (if condition is true loop terminates)")
print("else :   \n\tremaining body of the loop")
