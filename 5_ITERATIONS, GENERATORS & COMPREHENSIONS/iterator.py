# USING LOOP
print("For loop can be used to iterate lists, tuples, dictionariess, strings etc")
L = [2,3,4,5,6,8,9,10]
for num in L:
    if num%2==0:
        print(num," is even")
    else:
        print(num," is odd")

name = "narendra"
count = 0
for char in name:
    if char == 'a':
        count = count+1
        print("Letter 'a' in ",name," is repeated ",count," times")

# USING ITER
print("\n-------USING iter() ------\n")
L = [-1,2,3,-4,7,-2,8,-10,11]
P = []
N = []
t = iter(L) #iterating over object ie; list named L and naming as variable t
try:
    while(True):
        x = t.__next__()    # every element of t is x and assisgned next value as loop ends so moving next
        if x>0:             # comparing and appending values accordingly
            P.append(x)
        else:
            N.append(x)
except StopIteration:       # end of iteration prints outputs when no element left
    print("List L is: ",L,"\nPositive list P is: ",P,"\nNegative list N is: ",N)
