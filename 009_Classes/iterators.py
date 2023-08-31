for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {"one": 1, "two": 2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end="")

# 1
# 2
# 3
# 1
# 2
# 3
# one
# two
# 1
# 2
# 3
# The rain in Spain falls mainly in the plain.
# As they say in Finland, there's more than one way to roast a reindeer.
# You can see a lot just by looking.
