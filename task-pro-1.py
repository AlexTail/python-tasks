"""

Рекурсия: Сумма Чисел, Факториал, Фибоначчи

Recursion Functions

1) privet n times
2) Sum  1 + 2 + 3 + 4 + 5 = 15
3) Factorial 5! = 1 * 2 * 3 * 4 * 5 = 120
4) Fibonacci 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

"""



def privet(x):
    """ 1) """
    if x == 0:
        return
    else:
        print('Hello World', x)
        privet(x-1)

privet(10)



def sum(x):
    """ 2) """
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x + sum(x-1)

z = sum(5)
print(z)



def factorial(x):
    """ 3) """
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5))



def fi(x):
    """ 4) """
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fi(x-1) + fi(x-2)

print(fi(7))