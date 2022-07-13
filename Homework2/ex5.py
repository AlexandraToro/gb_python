# Реализуйте алгоритм перемешивания списка.
from random import randint


def get_list() -> list:
    my_list = []
    for i in range(10):
        my_list.append(randint(1, 100))
    print(my_list)
    return my_list


def mix_list(our_list: list):
    for i in range(len(our_list)):
        r = randint(0, len(our_list)-1)
        t = our_list[i]
        our_list[i] = our_list[r]
        our_list[r] = t
    print(our_list)


new_list = get_list()
mix_list(new_list)
