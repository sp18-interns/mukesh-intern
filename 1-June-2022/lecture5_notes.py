

import math

def find_area_circle(radius):
    area = math.pi*radius**2
    return area


def find_area_cylinder(radius, height):
    area_circle = find_area_circle(radius)
    area_cylinder = 2*area_circle + \
        2*radius*math.pi*height
    return area_cylinder




r = input("Enter radius => ")
print (r)

h = input("Enter height => ")
print (h)

h = float(h)
r = float(h)

area_cylinder = find_area_cylinder(r,h)

print ("Area of cylinder with radius {0:.1f} and height {1:.1f} is {2:.1f}".format(r,h,area_cylinder))

