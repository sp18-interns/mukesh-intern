

def find_rectangle_area(l,h):
    area = l*h
    return area

def find_rectangular_solid_area(l,w,h):
    area1 = find_rectangle_area(l,w)
    area2 = find_rectangle_area(l,h)
    area3 = find_rectangle_area(w,h)
    total_area = 2*area1 + 2*area2 + 2*area3
    return (total_area)
