# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint


def get_list() -> list:
    n = int(input('Введите количество элементов n = '))
    my_list = []
    for i in range(n):
        my_list.append(randint(-n, n))
    print(f'Полученный список:{my_list}')
    return my_list


def multi_num(bingo: list):
    elements = list(
        map(int, input('Введите номера позиций через пробел (любые от 1 до n): ').split()))
    print(f'Номера позиций для умножения:{elements}')
    result = 1
    for j in elements:
        result = result * bingo[j-1]
    print(f'Итог: {result}')


my_list = get_list()
multi_num(my_list)
