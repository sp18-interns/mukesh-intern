

def find_rectangle_area(l,h):
    area = l*h
    return area

def find_area_rectangular_solid(l,w,h):
    area1 = find_rectangle_area(l,w)
    area2 = find_rectangle_area(l,h)
    area3 = find_rectangle_area(w,h)
    total_area = 2*area1 + 2*area2 + 2*area3
    return (total_area)
    

area = find_area_rectangular_solid(10,12,15)

print (area)