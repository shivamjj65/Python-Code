# generator are functions that generate requisite sequene
# the values are generated as program proceeds
def generate20nums():
    print("Start")
    for i in range(20):
        print("value of i is: ",i)
        yield i
        print("Value of yield i is: ",i)

a = generate20nums()
for i in a:
    print(i)