matrix1 = [
  [1, 3, 4],
  [2, 5, 6],
  [4, 3, 2]
]

matrix2 = [
  [2, 6, 4],
  [3, 4, 2],
  [4, 2, 7]
]

result_matrix = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

for i in range(len(matrix1)):
  for j in range(len(matrix2)):
    result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

# to print the row of the result matrix
for row in result_matrix:
  print(row)
