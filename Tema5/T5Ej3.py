def isLeapYear(year: int) -> bool:
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print("El año {} es bisiesto".format(year))
    else:
        print("El año {} NO es bisiesto".format(year))


year = int(input("Introduce el año: "))
isLeapYear(year)