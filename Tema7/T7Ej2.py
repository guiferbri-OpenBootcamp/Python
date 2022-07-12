import time

current_time = time.localtime()
current_hour = current_time.tm_hour
current_min = current_time.tm_min

if current_hour >= 19:
    print("Hora de irse!")
else:
    rest_hour = 18 - current_hour
    rest_min = 59 - current_min
    print("Quedan {} horas y {} minutos".format(rest_hour, rest_min))