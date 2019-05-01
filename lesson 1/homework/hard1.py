name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
age = float(input('Введите ваш возраст: '))
weight = float(input('Введите ваш вес: '))

print('Ваши данные:\n' +
      'Имя - ' + name + '\n' +
      'Фамилия - ' + surname + '\n' +
      'Возраст - ' + str(age) + '\n' +
      'Вес - ' + str(weight))

if age < 30 and (50 < weight < 120):
    print('Хорошее состояние')
elif (30 < age < 40) and (weight < 50 or weight > 120):
    print('Необходимо заняться собой')
elif age > 40 and (weight < 50 or weight > 120):
    print('Следует обратиться к врачу')

