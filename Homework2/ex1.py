# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

def sum_of_number():
    num = input('Введите любое вещественое число: ')
    sum_num = 0
    for i in range(len(num)):
        if num[i] == ',' or num[i] == '.':
            sum_num = sum_num
        else:
            sum_num = sum_num + int(num[i])
    print(sum_num)


sum_of_number()