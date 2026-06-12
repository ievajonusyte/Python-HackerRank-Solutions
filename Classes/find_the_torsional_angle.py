import math

'''
You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system.
You are required to print the angle between the plane made by points A, B, C and
the plane made by points B, C, D. The angle should be in degrees (not radians).
Like the angle between two pages of an open book.

Formula: cos(PHI) = (X.Y) / (|X||Y|)
where X = AB x BC and Y = BC x CD
AB means vector from A to B (B - A), x means cross product, . means dot product.

Input: 4 lines, each with space-separated x y z float coordinates for points A, B, C, D.
Output: the angle PHI in degrees, correct to two decimal places.
'''

# Define a class to represent a point (or vector) in 3D space
class Points(object):
    
    # Called when you create a Point, e.g. Points(1.0, 2.0, 3.0)
    # Stores the three coordinates x, y, z on the object
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    # Called when you write "a - b" between two Points
    # Subtracts coordinate by coordinate, returns a new Point (which is now a vector)
    # e.g. B - A gives the vector pointing from A to B
    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)
        
    # Dot product of two vectors: multiply matching coordinates, then sum everything up
    # Returns a single number (not a Point)
    # Used later to find the angle: cos(angle) = dot product divided by (length times length)
    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)
    
    # Cross product of two vectors: returns a new vector perpendicular to both
    # This is how we find the normal vector sticking out of each plane
    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,  # x component
            self.z * no.x - self.x * no.z,  # y component
            self.x * no.y - self.y * no.x   # z component
        )
        
    # Length (magnitude) of the vector
    # Pythagoras extended to 3D: square root of (x*x + y*y + z*z)
    # Used in the denominator of the angle formula
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

  if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
