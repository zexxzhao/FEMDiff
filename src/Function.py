
from Cell import Cell
from Element import Element, ScalarElement, VectorElement


class GenericFunction:
    def __init__(self, element):
        self._elem = element

