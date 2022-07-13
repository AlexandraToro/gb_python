#     Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        return result


def list_factorial(n: int) -> list:
    my_list = []
    for i in range(1, n+1):
        my_list.append(factorial(i))
    return my_list


print(list_factorial(5))
