def isprimenumber(number: int) -> float:
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        return True
    return False


test1 = 7
result1 = isprimenumber(test1)
test2 = 12
result2 = isprimenumber(test2)
print("¿El número {} es primo?: {}".format(test1, result1))
print("¿El número {} es primo?: {}".format(test2, result2))

test3 = int(input("Introduce el número: "))
result3 = isprimenumber(test3)
print("¿El número {} es primo?: {}".format(test3, result3))