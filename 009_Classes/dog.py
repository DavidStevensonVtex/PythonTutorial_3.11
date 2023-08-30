class Dog:
    def __init__(self, name):
        self.name = name  # instance variable unique to each instance
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")

print("d.tricks", d.tricks)
print("e.tricks", e.tricks)

# d.tricks["roll over"]
# e.tricks["play dead"]
