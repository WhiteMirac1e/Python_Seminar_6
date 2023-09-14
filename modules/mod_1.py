# Создайте модуль и напишите в нём функцию, которая получает на
# вход дату в формате DD.MM.YYYY Функция возвращает истину, 
# если дата может существовать или ложь, если такая дата невозможна. 
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует 
# Григорианский календарь. Проверку года на високосность вынести в 
# отдельную защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

L = [1, 3, 5, 7, 8, 10, 12] # 31
S = [4, 6, 9, 11] # 30
F = [2] # 28

def input_date():
    day = input('Введите день: ')
    month = input('Введите месяц: ')
    year = input('Введите год: ')
    return day, month, year

def leap_year(year):
    if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
        return True
    else: 
        return False

def my_func(day, month, year, bl):
    if 1 <= year <= 9999:
        if 1 <= month <= 12:
            if month in L:
                if day <= 31:
                    return True
                else:
                    return False
            elif month in S:
                if day <= 30:
                    return True
                else:
                    return False
            elif month in F:
                if bl == True:
                    if day <= 29:
                        return True
                    else:
                        return False
                elif bl == False:
                    if day <= 28:
                        return True
                    else:
                        return False    
        else:
            return False
    else:
        return False
