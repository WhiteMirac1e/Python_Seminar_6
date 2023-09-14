# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from modules.mod_1 import leap_year
from modules.mod_1 import my_func
from modules.mod_1 import input_date
data = input_date()
day = int(data[0])
month = int(data[1])
year = int(data[2])
b = leap_year(year)
print(my_func(day, month, year ,b))
