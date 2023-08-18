matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

new_matrix = [[row[i] for row in matrix] for i in range(4)]
print(new_matrix)
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]


new_matrix = list(zip(*matrix))
print(matrix)
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(*matrix)
# [1, 2, 3, 4] [5, 6, 7, 8] [9, 10, 11, 12]
print(new_matrix)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
