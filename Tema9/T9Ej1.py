input_countries = input("Indique una lista de países separados por comas: ")
countries = set(input_countries.split(','))
order_countries = sorted(countries)
separator = ','
print(separator.join(order_countries))