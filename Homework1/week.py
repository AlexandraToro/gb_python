# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

n = int(input('Введите число от 1 до 7, соответствующее дню недели: '))
if (n > 0 and n < 8):
    if (n == 6 or n == 7):
        print('-> выходной день')
    else:
        print('-> будний день')
else:
    print('Введено некорректное значение')
