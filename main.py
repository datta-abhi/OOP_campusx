from atm import *
from fraction import *
from geometry import *

# testing atm
# atm1 = MyAtm()

# testing fractions
fr1 = Fraction(3,4)
fr2 = Fraction(6,7)

# print(fr1+fr2)
# print(fr1*fr2)
# ----------------------------------------------------------------------------
# testing geometry
p1 = Point(3,5)
p2 = Point(1,1)

d0 = p1.dist_from_origin()
d1 = p1.dist_bw_points(p2)
d2 = p2.dist_bw_points(p1)

l1 = Line(2,3,10)
ck2 = l1.point_on_line(p2)
ck1 = l1.point_on_line(p1)
short_dist = l1.shortest_distance(p1)

print(p1)
print(p2)
print(d0)
print(d1)
print(d2)
print(l1)
print(ck1)
print(ck2)
print(short_dist)

# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------
