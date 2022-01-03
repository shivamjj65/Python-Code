'''Principles of OOPs:
Class
Object
Method
Inheritance
Polymorphism
Data Abstraction
Encapsulation

Class:
The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods.
We can also say that class is a blueprint of an object i.e. if any person is an object, class will have all the information about the structure or behaviour that person.
OOPs, reduce the size of our code.

Object:
Object is a simple entity which posses some property or behaviour.
Everything in Python is an object, and almost everything has attributes and methods.

Method:
The method is a function that is associated with an object.
In Python, a method is not unique to class instances. Any object type can have methods.
'''

class Student:
    def __init__(self,roll,name,age):
        self.roll = roll
        self.name = name
        self.age = age
    def display(self):
        print("Age of",self.name," is :",self.age)

object1 = Student(1,'Narendra',20)
object1.display()
object2 = Student(2,'Amit',19)
object2.display()