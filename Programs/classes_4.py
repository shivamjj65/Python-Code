# example

class Human:
    x=5
    name="modi"

h1 = Human()
print(h1.x)
print(h1.name)


# ex2
# init func. is basically something executed when class is initialized
class H:
    def __init__(self,age,name):
        self.age = age
        self.name = name

    def method(self):
        print("\n Mitron mai "+ self.name +" aapse vaada karta hun ki Achhe Din Aayege !")


h2 = H(57,"Narendra Modi")
h2.method()