import matplotlib.pyplot as plt


class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __repr__(self):
        """Return this point/vector as a string in the form "(x, y)" """
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

        
class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0


def simple_polygon(points):
    # Anchor point
    bottommost = min(points, key=lambda p: (p.y, p.x))
    #Compute and sort the angle of from the bottom most point
    sorted_points = sorted(points, key=lambda p: PointSortKey(p, bottommost))
    return sorted_points

# points = [
#     Vec(100, 100),
#     Vec(0, 100),
#     Vec(50, 0)]
# verts = simple_polygon(points)
# for v in verts:
#     print(v)


# points = [
#     Vec(100, 100),
#     Vec(0, 100),
#     Vec(100, 0),
#     Vec(0, 0),
#     Vec(49, 50)]
# verts = simple_polygon(points)
# for v in verts:
#     print(v)

def plot_polygon(points):
    plt.figure()
    plt.plot([p.x for p in points + points[:1]], [p.y for p in points + points[:1]], 'r-')
    plt.scatter([p.x for p in points], [p.y for p in points])
    plt.show()


points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(50, 0)]
verts = simple_polygon(points)
plot_polygon(verts)

points = [
    Vec(100, 100),
    Vec(0, 100),
    Vec(100, 0),
    Vec(0, 0),
    Vec(49, 50)]
verts = simple_polygon(points)
plot_polygon(verts)