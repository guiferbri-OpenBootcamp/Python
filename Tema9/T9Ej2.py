from functools import reduce

def oddElements(x):
    return x % 2 == 1


elementsList = list(range(52))
odd = filter(oddElements, elementsList)
addOddElements = reduce(lambda x, y: x + y, odd)
print(addOddElements)