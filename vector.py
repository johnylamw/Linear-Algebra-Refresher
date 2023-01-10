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
    
    # 4. __add__, __sub__, __mul__ 
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
    
    # 6. Magnitude & Direction
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
        
    # 8. Dot Product & Angle
    def dot_product(self, w):
        sum = 0
        for point in range(len(self.coordinates)):
            sum += self.coordinates[point] * w.coordinates[point]
        return sum

    # Returns the angle between two vectors in radians/degrees
    def angle_with(self, w, in_degrees=False):
            result = math.acos(self.dot_product(w) / (self.magnitude() * w.magnitude())) # in radians
            if in_degrees:
                result *= 180/math.pi
            return result

# TODO: Clean up exercises code to look better by instantiating vectors.
# 4. Vector Plus, Minus and Scalar Multiply
print('\nExercise 4:')
print(Vector([8.218, -9.341]) + Vector([-1.129, 2.111]))
print(Vector([7.119, 8.215]) - Vector([-8.223, 0.878]))
print(Vector([1.671, -1.012, -0.318]) * 7.41)

print('\nExercise 6:')
# 6. Magntiude and Direction
print(Vector([-0.221, 7.437]).magnitude())
print(Vector([8.813, -1.331, -6.247]).magnitude())
print(Vector([5.581, -2.136]).normalized())
print(Vector([1.996, 3.108, -4.554]).normalized())

# 8. Dot Product & Angle
print('\nExercise 8:')
print(Vector([7.887, 4.138]).dot_product(Vector([-8.802, 6.776])))
print(Vector([-5.955, -4.904, -1.874]).dot_product(Vector([-4.496, -8.755, 7.103])))
print(Vector([3.183, -7.627]).angle_with(Vector([-2.668, 5.319])), 'radians')
print(Vector([7.35, 0.221, 5.188]).angle_with(Vector([2.751, 8.259, 3.985]), True), 'degrees')