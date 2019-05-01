a = int(input('Введите число a: '))
b = int(input('Введите число b: '))

print('Ваши числа: ' + str(a) + ' и ' + str(b))

a = a + b
b = a - b
a = a - b

print('Поменяли числа местами: теперь а =', str(a), ' и b =', str(b))