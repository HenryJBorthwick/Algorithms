class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        """String representation of self"""
        return "({}, {})".format(self.x, self.y)
        

class QuadTree:
    """This class represents a QuadTree, which is a tree data structure used 
    to efficiently locate points within a two-dimensional space."""
    
    # This is a predefined constant that defines the maximum depth of the tree.
    MAX_DEPTH = 20

    def __init__(self, points, centre, size, depth=0, max_leaf_points=2):
        # This is the constructor, it sets up the initial state of the QuadTree.
        
        # The center of the square representing this part of the quad tree.
        self.centre = centre

        # The size of the square representing this part of the quad tree.
        self.size = size

        # The depth of this node in the tree.
        self.depth = depth

        # The maximum number of points a leaf node can hold before it needs to split into more nodes.
        self.max_leaf_points = max_leaf_points

        # Initialize as not a leaf.
        self.is_leaf = False

        # The four child nodes of this node (if any). Starts off empty.
        self.children = []
        
        # Collects points that fall within this square.
        self.points = [p for p in points if abs(p.x - centre.x) <= size / 2 and abs(p.y - centre.y) <= size / 2]
        
        # If too many points for this node or the maximum depth is reached, the node is divided further.
        if len(self.points) > self.max_leaf_points and self.depth < self.MAX_DEPTH:
            quad_size = size / 2

            # The centers of the four new child squares are calculated.
            centres = [Vec(centre.x - quad_size / 2, centre.y - quad_size / 2),
                       Vec(centre.x - quad_size / 2, centre.y + quad_size / 2),
                       Vec(centre.x + quad_size / 2, centre.y - quad_size / 2),
                       Vec(centre.x + quad_size / 2, centre.y + quad_size / 2)]
            
            # Creates the new child nodes.
            for quad_centre in centres:
                self.children.append(QuadTree(points, quad_centre, quad_size, self.depth + 1, self.max_leaf_points))
            
            # Remove points that have been put into child nodes from this node.
            self.points = [p for p in self.points if not any(child.contains(p) for child in self.children)]
        else:
            # If no further division is necessary, this is a leaf node.
            self.is_leaf = True

    def contains(self, point):
        """Check if a point is inside the square of this quad tree"""
        
        # Checks whether a given point falls within the boundaries of this square.
        return abs(point.x - self.centre.x) <= self.size / 2 and abs(point.y - self.centre.y) <= self.size / 2
    

    def plot(self, axes):
        """Plot the dividing axes of this node and
           (recursively) all children"""
        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
        else:
            axes.plot([self.centre.x - self.size / 2, self.centre.x + self.size / 2],
                      [self.centre.y, self.centre.y], '-', color='gray')
            axes.plot([self.centre.x, self.centre.x],
                      [self.centre.y - self.size / 2, self.centre.y + self.size / 2],
                      '-', color='gray')
            for child in self.children:
                child.plot(axes)
        axes.set_aspect(1)
                
    def __repr__(self, depth=0):
        """String representation with children indented"""
        indent = 2 * self.depth * ' '
        if self.is_leaf:
            return indent + "Leaf({}, {}, {})".format(self.centre, self.size, self.points)
        else:
            s = indent + "Node({}, {}, [\n".format(self.centre, self.size)
            for child in self.children:
                s += child.__repr__(depth + 1) + ',\n'
            s += indent + '])'
            return s
        
import matplotlib.pyplot as plt
points = [(60, 15), (15, 60), (30, 58), (42, 66), (40, 70)]
vecs = [Vec(*p) for p in points]
tree = QuadTree(vecs, Vec(50, 50), 100)
print(tree)

# Plot the tree, for debugging only
axes = plt.axes()
tree.plot(axes)
axes.set_xlim(0, 100)
axes.set_ylim(0, 100)
plt.show()

# Node((50, 50), 100, [
#   Leaf((25.0, 25.0), 50.0, []),
#   Node((25.0, 75.0), 50.0, [
#     Leaf((12.5, 62.5), 25.0, [(15, 60)]),
#     Leaf((12.5, 87.5), 25.0, []),
#     Node((37.5, 62.5), 25.0, [
#       Leaf((31.25, 56.25), 12.5, [(30, 58)]),
#       Leaf((31.25, 68.75), 12.5, []),
#       Leaf((43.75, 56.25), 12.5, []),
#       Leaf((43.75, 68.75), 12.5, [(42, 66), (40, 70)]),
#     ]),
#     Leaf((37.5, 87.5), 25.0, []),
#   ]),
#   Leaf((75.0, 25.0), 50.0, [(60, 15)]),
#   Leaf((75.0, 75.0), 50.0, []),
# ])