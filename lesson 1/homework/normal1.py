# user_number = int(input('Введите число больше 0 и меньше 10: '))

# if user_number < 0 or user_number > 10:
#     print('Введите число больше 0 и меньше 10')
# else:
#     print(user_number ** 2)


while True:
    user_number = int(input('Введите число больше 0 и меньше 10: '))
    if user_number < 0 or user_number > 10:
        print('Вы ввели неверное число')
        continue
    else:
        print(user_number ** 2)
        break


# while True:
#     user_number = int(input('Введите число больше 0 и меньше 10: '))
#     if 0 < user_number < 10:
#         print(user_number ** 2)
#         break
#     else:
#         print('Вы ввели неверное число')