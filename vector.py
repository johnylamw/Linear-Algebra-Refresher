import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    def __add__(self, v):
        result = []
        for i in range(len(self.coordinates)):
            result.append(self.coordinates[i] + v.coordinates[i])
        return Vector(result)
    
    def __sub__(self, v):
        result = []
        for i in range(len(self.coordinates)):
            result.append(self.coordinates[i] - v.coordinates[i])
        return Vector(result)
    
    def __mul__(self, s):
        result = []
        for i in range (len(self.coordinates)):
            result.append(s * self.coordinates[i])
        return Vector(result)
    
    def magnitude(self): 
        result = 0
        for value in self.coordinates:
            result += value ** 2
        return math.sqrt(result)    
    
    def normalized(self):
        try:
            scalar = 1 / self.magnitude()
            return self * scalar
        except:
            raise Exception('Cannot normalize the zero vector')

# 4. Vector Plus, Minus and Scalar Multiply
print(Vector([8.218, -9.341]) + Vector([-1.129, 2.111]))
print(Vector([7.119, 8.215]) - Vector([-8.223, 0.878]))
print(Vector([1.671, -1.012, -0.318]) * 7.41)

# 6. Magntiude and Direction
print(Vector([-0.221, 7.437]).magnitude())
print(Vector([8.813, -1.331, -6.247]).magnitude())
print(Vector([5.581, -2.136]).normalized())
print(Vector([1.996, 3.108, -4.554]).normalized())
