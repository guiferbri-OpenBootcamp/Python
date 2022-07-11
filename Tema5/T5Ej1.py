import math
def triangleArea(high : float, base : float) -> float:
    area = (base * high) / 2
    return area

def circleArea(radio : float) -> float:
    area = math.pi * math.pow(radio, 2)
    return area

high = 2
base = 3
areaT = triangleArea(high, base)
print("Área del triángulo de altura {} y base {}: {}".format(high, base, areaT))
radio = 5
areaC = circleArea(high)
print("Área del círculo de radio {}: {}".format(radio, areaC))