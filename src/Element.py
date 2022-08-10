

from Cell import Cell

class Element:
    def __init__(self, cell, num_value):
        self._cell = cell
        self._nval = num_value

    def is_scalar(self):
        return self._nval == 1

    def is_vector(self):
        return self._nval > 1


class ScalarElement(Element):
    def __init__(self, cell):
        super().__init__(cell, 1)

class VectorElement(Element):
    def __init__(self, cell):
        super().__init__(cell, cell.dim())
