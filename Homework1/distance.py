#     Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#     Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt
x1 = int(input('Введите значение координаты х первой точки: '))
y1 = int(input('Введите значение координаты y первой точки: '))
x2 = int(input('Введите значение координаты х второй точки: '))
y2 = int(input('Введите значение координаты y второй точки: '))
d = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
print(round(d, 2))
