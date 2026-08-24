## Example

import collections as cl

Point = cl.namedtuple('Point', ['x', 'y'], defaults=[0,0])
p1 = Point(3,4)
p2 = Point()
print(p1, p1.x, p1.y)
print(p2)


