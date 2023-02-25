# Calculate the minimum distance to point(0,0)
# from the points list.

import math
points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]
dist = []
for(x,y) in points:
    s = math.sqrt(x*x + y*y)
    dist.append(s)
print(min(dist))

# Answer using list comprehension

points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]
print(min([(a**2+b**2)**(1/2) for a, b in points]))