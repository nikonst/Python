# OOP Basic Concepts

class Person:
    species = "Human" # Class field

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def introduceYourself(self):
        print("Hi! My name is ", self.name)

    def myFavouriteMovie(self):
        print("Terminator I")

class Employee(Person): # Inheritance
    def __init__(self, name,gender,profession):
        super().__init__(name, gender)
        self.profession = profession
        self.__salary = 1000 # Encapsulation

    def sayProfession(self):
        print("I am a ", self.profession)

    def showSalary(self):
        print("My salary is ", self.__salary)

    def myFavouriteMovie(self): # Polymorphism
        print("Terminator II")

def showFavouritMovie(p):
    p.myFavouriteMovie()

p1 = Person("Mary","female")
p1.introduceYourself()

p2 = Employee("Nick","Male","Carpenter")
p2.introduceYourself()
p2.sayProfession()

print("----------------------")

print(p1.name)
#print(p2.__salary) # salary is a private field
p2.showSalary()

print("----------------------")

print(p1.species)
print(p2.species)

print("----------------------")

showFavouritMovie(p1)
showFavouritMovie(p2)


