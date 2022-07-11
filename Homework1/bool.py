# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z    1 выражение  2 выражение')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            equation1 = not (x or y or z)
            equation2 = not x and not y and not z
            print(x, y, z, '  ', equation1, '      ', equation2)
if equation1 == equation2:
    print('Утверждение (¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) истинно')
else:
    print('Утверждение (¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z) ложно')
