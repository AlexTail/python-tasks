"""
Дано целое число some_number (до 1000), которое вводится с клавиатуры. Вернуть
наибольшее число, содержащее ровно some_number цифр.
"""


# if some_number == 3
#   return 999

# if some_number == 5
#   return 99999

# if some_number == 1
#   return 9

# if some_number == 0
#   return 0



# Решение №1 -----------------------------------------------------------

print(int("9"*int(input('1) Введите целое число до 1000: '))))



# Решение №2 -----------------------------------------------------------

def max_number(some_number: int) -> int:
    return 10 ** some_number - 1

print(max_number(int(input('2) Введите целое число до 1000: '))))



