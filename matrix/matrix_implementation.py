from typing import Tuple


class Matrix:
    def __init__(self, m, parameter=0):
        if isinstance(m, Tuple):
            self.matrix = [[parameter for i in range(m[1])] for k in range(m[0])]
        else:
            self.matrix = m

    def size(self):
        return len(self.matrix), len(self.matrix[0])

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, other_matrix):
        if Matrix.size(self) == Matrix.size(other_matrix):
            sum_of_matrix = Matrix((len(self.matrix), len(self.matrix[0])))
            for i in range(len(self.matrix)):
                for k in range(len(self.matrix[0])):
                    sum_of_matrix[i][k] = self.matrix[i][k] + other_matrix[i][k]
            return sum_of_matrix
        else:
            raise Exception("matrix has different dimensions")

    def __mul__(self, other_matrix):
        if Matrix.size(self)[0] == Matrix.size(other_matrix)[1]:
            multiple_of_matrix = Matrix((len(other_matrix[0]), len(self.matrix)))
            for i in range(len(self.matrix)):
                for k in range(len(other_matrix[0])):
                    for m in range(len(self.matrix[0])):
                        multiple_of_matrix[i][k] += self.matrix[i][m] * other_matrix[m][k]
            return multiple_of_matrix
        else:
            raise Exception("incorrect matrix dimensions")

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += str(row) + "\n"
        result = "[" + result + "]"
        return result


def matrix_transposition(z: Matrix):
    result = Matrix((z.size()[1], z.size()[0]))
    for i in range(z.size()[1]):
        for k in range(z.size()[0]):
            result[i][k] = z[k][i]
    return Matrix(result)


A = Matrix([[1, 0, 2], [-1, 3, 1]])
B = Matrix([[3, 1], [2, 1], [1, 0]])
C = Matrix((2, 3), parameter=1)
print(matrix_transposition(A))
print(A + C)
print(A * B)
