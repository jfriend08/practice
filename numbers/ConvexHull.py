'''
Convex Hull | Set 1 (Jarvis's Algorithm or Wrapping)

Given a set of points in the plane. the convex hull of the set is the smallest
convex polygon that contains all the points of it.
'''

def orientation(p, q, r):
  val =  (r[0]-q[0]) * (q[1]-p[1]) - (q[0]-p[0]) * (r[1]-q[1])
  if val == 0:
    return 0
  return (2 if val < 0 else 1)

def getConvexPoints(points):
  points = sorted(points, key = lambda x: x[0])
  l, p, q = points[0], points[1], points[1]
  res = [q]
  while p != l:
    q = points[1]
    for r in points:
      if orientation(p, r, q) == 2:
        q = r
    p = q
    print "hi",p, q, l
    res += [p]
  return res

points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
print getConvexPoints(points)
