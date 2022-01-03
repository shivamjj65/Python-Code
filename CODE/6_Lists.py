'''
print("\nData-types and some functions")
print("--------LISTS-----------")
print("Lists are used to store data in a single variable. "
      "Lists in python is same as arrays , the only difference is arrays store only homogeneous type of elements "
      "(say all elements must only be integers , float , string) "
      "but in lists it stores heterogeneous type of elements. Lists are mutable and indexed where index starts from "
      "zero.")
print(
    "Lists are indexed, Lists are mutable, Lists allow duplicates, Lists can store heterogeneous datatypes, "
    "Lists can be used as nested format ")

print("\nEXAMPLE")

arr = list()
n = eval(input("Enter size of list : "))
print("Enter data to be filled: ")
for i in range(0, n):
    a = input()
    arr.append(a)  # append func will take a and fill it in arr
print("Your list is : ", arr)

arr.insert(1, "kiwi")  # inserting kiwi at 1st index ie; arr[1]
print(arr)  # after insert size of list will dynamically increase

arr.sort()
print("List after sort is :", arr)

arr.reverse()
print("Reversed list is :", arr)

# deleting items in list

# pop means deleting from index 
j = eval(input("Enter index: "))
print("Deleting the", j, "index in list", arr.pop(j))
print(arr)

# remove used to remove a particular list element
print(arr)
x = input("Enter value to be removed")
arr.remove(x)

# del used to delete set of elements
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
print("Removing 1 to 5 by using a.del[1:3]")
del(a[1:3])
print(a)

# clear used to clear entire list
print(a.clear())

'''
'''  NESTED LISTS  '''
# ex : [[1,2,3],[4,5,6]]
# 2x2 matrix
matrix1 = [[1, 2], [3, 4]]
for i in range(2):
    print(matrix1[i])
# i x y matrix
rows = eval(input("Enter no of rows"))
cols = eval(input("Enter no of columns"))
matrix2 = []
for i in range(rows):
    for j in range(cols):
        value = input()
        matrix2.append(value)

print("The matrix of size", rows,"x", cols, "is")
for i in range(rows):
    for j in range(cols):
        print(matrix2[i][j])
