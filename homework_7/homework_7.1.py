class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([' '.join(map(str, matrix)) for matrix in self.matrix])

    def __add__(self, other):
        return Matrix(list(map(lambda i, j: list(map(lambda x, y: x + y, i, j)), self.matrix, other.matrix)))



matrix_1 = Matrix([[31, 22, 44], [37, 43, 65], [51, 86, 86]])

print (matrix_1, '\n')

matrix_2 = Matrix([[31, 22, 44], [37, 43, 65], [51, 86, 86]])

print (matrix_1 + matrix_2)