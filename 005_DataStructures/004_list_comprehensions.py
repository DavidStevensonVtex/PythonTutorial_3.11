squares = []
for x in range(10):
    squares.append(x**2)

print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares = list(map(lambda x: x**2, range(10)))
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

points = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(points)
# [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]

from math import pi

mypi = [str(round(pi, i)) for i in range(1, 6)]
print(mypi)
# ['3.1', '3.14', '3.142', '3.1416', '3.14159']
