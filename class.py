### everything in Python is an object 

## everything a list , tupel , string , dictionary, numbers , floats
## all of these things are instances of a class 

print(type([]))


[].append('something')

## slef is basically this in javascript 

## self is reffering each unique instance of the class 

class Dog():

    totalDogs = 0

    def __init__(self, name="", age=8, color=""):
        self.name = name
        self.age = age
        self.color = color

        print(name, "created: ", self)

    def bark_hello(self): 
        print("Woof! I am called", self.name, "and I am", self.age)

    def get_total_dogs(self):
        print("there are ", Dog.totalDogs, "made from this class")

franklin = Dog('Franklin', 4)
gunner = Dog('Gunner', 10)

print(franklin)

## with instances of a class we can use the dot notation 
## to access it's properties 

franklin.bark_hello()

print(gunner.bark_hello())

print(franklin.name)

## Instance variables - each thing that is attached to self is an instance variable 

## Clas variable = They are attach to the lass itself so theres one single
## thing that exist for the entire class 

class Parent():
    def __init__(self):
        self.first_name = 'Jim'
        self.last_name = 'haff'

    def hello(self):
        print(f"Hey i'm {self.first_name}. Welcome to my home")
    
    def get_first_name(self):
        return self.first_name

    def set_first_name(self, name):
        self.first_name = name
        return self.name

    def __str__(self):
         
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.first_name = "Baby frank"
        print("Child initialized", self)

    def hello(self):
        print(f"I'm {self.first_name}, im busy in class bro")

mom = Parent()
daughter = Child()
mom.hello()
daughter.hello()
print(daughter.last_name)

