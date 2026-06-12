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

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)
        
    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,  # x component
            self.z * no.x - self.x * no.z,  # y component
            self.x * no.y - self.y * no.x   # z component
        )
    
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
