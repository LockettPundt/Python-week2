#First class on OOP (Object Oriented Programming) 1/21/20.
#creating a constructor and an instance of the class.

class Cat:
    species = "mammal"
    legs = 4
    eyes = 2
    tail = 1

    def __init__(self, name, age, color, temperment, location):
        self.name = name
        self.age = age
        self.color = color
        self.temperment = temperment
        self.location = location

    def description(self):
        return "Hi there. My name is {}, and I'm a {}, {} year old cat.".format(self.name, self.color, self.age)

    def temp_loc(self):
        return "I'm typically {} and I live in {}".format(self.temperment, self.location)
    
    def eat(self):
        return "I love to eat {}".format(self.food)

sam = Cat("Sam", 10, "Grey", "happy", "Atlanta")
chloe = Cat("Chloe", 15, "tabby", "grumpy", "Atlanta")

#added a "food" attribute to sam. 
sam.food = "ice cream"

print("{}, {}, {}".format(sam.name, sam.age, sam.color))
print(sam.description(), sam.temp_loc())
print(sam.eat())

print("{}, {}, {}".format(chloe.name, chloe.age, chloe.color))
print(chloe.description(), chloe.temp_loc())


