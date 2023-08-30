class Dog:
    tricks = []  # mistaken use of a class variable

    def __init__(self, name):
        self.name = name  # instance variable unique to each instance

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog("Fido")
e = Dog("Buddy")
d.add_trick("roll over")
e.add_trick("play dead")

print("d.tricks", d.tricks)  # unexpectedly shared by all dogs
# d.tricks ['roll over', 'play dead']
