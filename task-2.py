"""
Имеется положительное число. Необходимо найти сумму его цифр. Если
передается не число, вернуть 'Это не число!'
"""

# Если some_number == 45
# то 9

# Если some_number == 425
# то 11

# Если some_number == 1231421
# то 14

# Если some_number == {'key' : 'value'}
# то 'Это не число!'

some_number = 1231421

def sum_of_numbers(number):
        len_of_numbers = len(str(number))
        result = 0
        for n in range(len_of_numbers):
            result += int(str(number)[n])
        return result

print('Сумма =', sum_of_numbers(some_number))



        
    

