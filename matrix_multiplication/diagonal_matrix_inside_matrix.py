from typing import List
from matrix import DiagonalMatrix

TypeMatrix = List[DiagonalMatrix]


class CompositeMatrix:
    """
    A matrix that contain a collection of unique diagonal matrices
    """
    def __init__(self, matrix: TypeMatrix):
        self.matrix = matrix

    def __mul__(self, multiplier_matix: TypeMatrix):
        """
        Multiply two composite matrix
        """
        ...

    def inverse(self):
        """
        Get inverse
        """
        

    def __repr__(self):
        pass