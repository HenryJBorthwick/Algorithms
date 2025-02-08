class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
        
        
def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

# def is_on_segment(p, a, b):
#     # First, check if point p, a, and b are collinear.
#     # The signed area of the triangle formed by a, b, and p would be 0
#     # if they are collinear.
#     if signed_area(a, b, p) != 0:
#         return False

#     # Second, check if the x-coordinate and y-coordinate of p lie within
#     # the range of x-coordinates and y-coordinates of a and b.
#     # The point p should not be outside the line segment from a to b.

#     # Check if p's x-coordinate is between a's and b's x-coordinates
#     if not (min(a.x, b.x) <= p.x <= max(a.x, b.x)):
#         return False

#     # Check if p's y-coordinate is between a's and b's y-coordinates
#     if not (min(a.y, b.y) <= p.y <= max(a.y, b.y)):
#         return False

#     # If both checks passed, then p is indeed on the line segment from a to b.
#     return True

def is_on_segment(p, a, b):
    # Check if points are collinear
    if signed_area(a, b, p) != 0:
        return False

    # Compute squared lengths of vectors
    length_squared_pa = (p - a).lensq()
    length_squared_pb = (p - b).lensq()
    length_squared_ab = (a - b).lensq()

    # Check if PA and PB are less than or equal to AB
    if length_squared_pa > length_squared_ab or length_squared_pb > length_squared_ab:
        return False

    # If all checks passed, then p is indeed on the line segment from a to b.
    return True


a = Vec(1000, 2000)
b = Vec(0, 0)
p = Vec(500, 1000)
print(is_on_segment(p, a, b))

a = Vec(0, 0)
b = Vec(1000, 2000)
point_tuples = [
    (-1, -1),
    (-1, -2),
    (-1000, -2000),
    (0, 0),
    (1, 2),
    (500, 1000),
    (500, 1001),
    (500, 999),
    (1000, 2000),
    (1001, 2001),
    (1001, 2002),
    (2000, 4000)]
points = [Vec(p[0], p[1]) for p in point_tuples]
for p in points:
    print(p, is_on_segment(p, a, b))