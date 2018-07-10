# OOP Multiple Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printNameAge(self):
        print("My name is ", self.name, ". I am ", self.age, "years old.")

class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def printSport(self):
        print("My sport is ", self.sport)

class Player(Person, Athlete):
    def __init__(self, name, age, sport):
        Person.__init__(self,name, age)
        Athlete.__init__(self,sport)

    def introduceYourself(self):
        Person.printNameAge(self)
        Athlete.printSport(self)

p = Player("Thomas","27","football")
p.introduceYourself()
