"""
Имеется положительное число. Необходимо найти сумму его цифр. Если
передается не число, вывести 'Это не число!'
"""

# Если some_number == 45
# то 9

# Если some_number == 425
# то 11

# Если some_number == 1231421
# то 14

# Если some_number == {'key' : 'value'}
# то 'Это не число!'



# Решение № 1 ----------------------------------------------------------
num = input("1) Введите число: ")

if num.isnumeric():
        print('1) Cумма чисел: ', sum(map(int, num)))
else:
        print("1) Это не число!")
print('\n')



# Решение № 2 ----------------------------------------------------------

some_number = 197

def sum_of_digits(number: int):
        if str(number).isnumeric():
                print(type(number))
                digit_list = map(int, str(number))
                print('2) Cумма чисел: ', sum(digit_list))
        else:
                print("2) Это не число!")
                
sum_of_digits(some_number)
print('\n')



# Решение № 3 ----------------------------------------------------------

some_num = 197

def sum_of_digits(number: int):
    if str(number).isnumeric():
        print('3) Cумма чисел: ', sum([int(i) for i in str(number)]))
    else:
        print("3) Это не число!")
sum_of_digits(some_num)
print('\n')



# Решение № 4 ----------------------------------------------------------

some_number = input("4) Введите число: ")

def sum_of_numbers(number: str):
        if number.isnumeric():
                len_of_numbers = len(number)
                result = 0
                for n in range(len_of_numbers):
                    result += int(number[n])
                print('4) Сумма чисел =', result)
        else:
                print("4) Это не число!")


sum_of_numbers(some_number)
