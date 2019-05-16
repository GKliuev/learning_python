# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

number = 9782345
number = str(number)
# for index, number in enumerate(number):
#     print(number)
index = 0
while index < len(number):
    print(number[index])
    index += 1