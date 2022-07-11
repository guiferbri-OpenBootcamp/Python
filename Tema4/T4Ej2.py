num_init = int(input("Número inicial:"))
num_end = int(input("Número final:"))

while num_end < num_init:
    num_end = int(input("El número final debe ser mayor que el inicial. Introduzca un nuevo número final:"))

odd_numbers = []
for num in range(num_init, num_end+1):
    if num % 2 == 1:
        odd_numbers.append(num)

print("Número impares entre {} y {}: {}".format(num_init, num_end, odd_numbers))