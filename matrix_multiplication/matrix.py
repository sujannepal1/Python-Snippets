import numpy as np
from numpy.linalg import inv as inverse_matrix

INVALID_DIAGONAL_LENGTH = "Number of columns in the first matrix must be equal to the number of rows in the second matrix."


class Matrix:
    """
    Defaults to diagonal Matrix
    """

    def __init__(self, matrix: list[int] | list[list[int]], is_diagonal=True):
        self.matrix = np.array(matrix)
        self._is_diagonal = is_diagonal

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only multiply with another Matrix.")

        if not self._is_diagonal or not other._is_diagonal:
            raise ValueError(
                "Only diagonal matrices are supported as per the premises."
            )

        if len(self.matrix) != len(other.matrix):
            raise ValueError(INVALID_DIAGONAL_LENGTH)

        result = self.matrix * other.matrix
        return Matrix(result)

    def __repr__(self):
        if self._is_diagonal:
            return "\n".join(str(row) for row in np.diag(self.matrix))
        return "\n".join(str(row) for row in self.matrix)

    def inverse_matrix(self):
        array = np.diag(self.matrix)
        return inverse_matrix(array)


matrix_a = Matrix([1, 2, 3])
matrix_b = Matrix([1, 1, 1])

matrix_c = matrix_a * matrix_b

print(matrix_c)

print(matrix_c.inverse_matrix())
