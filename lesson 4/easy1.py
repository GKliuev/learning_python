# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

import random

# num_list = [random.randint(-10, 10) for _ in range(4)]
num_list = []
for i in range(4):
    num_list.append(random.randint(-10, 10))
print('List of numbers =', num_list)
# squared_list = [el ** 2 for el in num_list]
squared_list = []
for el in num_list:
    squared_list.append(el ** 2)
print("Squared list of numbers =", squared_list)