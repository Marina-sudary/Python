from math import ceil


def square(x, y):
    return ceil(x*y)


x = float(input('Введите длину первой стороны: '))
y = float(input('Введите длину второй стороны: '))


print(f'Округленная в большую сторону площадь - {square(x, y)}')
