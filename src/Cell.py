from abc import ABC

class Cell(ABC):
    def __init__(self, dim, num_vertices, num_facets):
        self._dim = dim
        self._nvtx = num_vertices
        self._nfacet = num_facets
    
    def dim(self):
        return self._dim

    def num_vertices(self):
        return self._nvtx

    def num_facets(self):
        return self._nfacet

    def is_simplex(self):
        raise NotImplementedError()

    def is_lagrangian_element(self):
        return True


class Line(Cell):
    def __init__(self):
        super().__init__(1, 2, 2)

    def is_simplex(self):
        return True

class Triangle(Cell):
    def __init__(self):
        super().__init__(2, 3, 3)

    def is_simplex(self):
        return True

class Quadrilateral(Cell):
    def __init__(self):
        super().__init__(2, 4, 4)

    def is_simplex(self):
        return False

class Tetrahedron(Cell):
    def __init__(self):
        super().__init__(3, 4, 4)

    def is_simplex(self):
        return True

class Hexahedron(Cell):
    def __init__(self):
        super().__init__(3, 8, 6)

    def is_simplex(self):
        return False

class Prism(Cell):
    def __init__(self):
        super().__init__(3, 6, 5)

    def is_simplex(self):
        return False

class Pyramid(Cell):
    def __init__(self):
        super().__init__(3, 5, 5)

    def is_simplex(self):
        return False

class IGA2(Cell):
    def __init__(self):
        super().__init__(3, 27, 1)

    def is_simplex(self):
        return False

    def is_Lagrangian_element(self):
        return False
