class Vec:
    """A simple vector in 2D. Also use for points (position vector)"""
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
        
        
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    p = b - a
    q = c - a
    area = p.x * q.y - q.x * p.y
    # May want to throw an exception if area == 0
    return area > 0 

def is_strictly_convex(vertices):
    # If there are fewer than 3 vertices, return False
    if len(vertices) < 3:
        return False

    # For each triplet of vertices
    for i in range(len(vertices)):
        # Get the current vertex, the next one, and the one after that
        a = vertices[i]
        b = vertices[(i + 1) % len(vertices)]
        c = vertices[(i + 2) % len(vertices)]

        # Check if the turn at 'b' is counter-clockwise. In other words, 
        # check if the interior angle at 'b' is less than 180 degrees. 
        # If it's not, the polygon is not strictly convex.
        if not is_ccw(a, b, c):
            return False

    # If all turns are counter-clockwise (i.e., all interior angles are 
    # less than 180 degrees), the polygon is strictly convex.
    return True


verts = [
    (0, 0),
    (100, 0),
    (100, 100),
    (0, 100)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))

verts = [
    (0, 0),
    (0, 100),
    (100, 100),
    (100, 0)]
points = [Vec(v[0], v[1]) for v in verts]
print(is_strictly_convex(points))