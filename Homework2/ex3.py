# Задайте список из n чисел последовательности (1 + 1/n)^n. и выведите на экран их сумму.
# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def sum_num(n: int) -> int:
    m_list = []
    sum = 0
    for i in range(1, n+1):
        m_list.append(round(pow((1+1/i), i), 2))
    print(m_list)       # код вставлен для проверки
    for i in m_list:
        sum = sum + i
    return sum          # можно написать print(sum), если в дальнейшем данное значение нам не понадобится
    

n = int(input('Введите число элементов последовательности: '))
print(sum_num(n))
