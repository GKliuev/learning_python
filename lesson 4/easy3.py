# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random

def is_correct(number):
  return (number % 3 == 0) & (number > 0) & (number % 4 > 0)


num_list = [random.randint(-10, 10) for _ in range(10)]
print("Number list =", num_list)
# result_list = [el for el in num_list if is_correct(el)]
result_list = []
for el in num_list:
    if is_correct(el):
        result_list.append(el)
print("Result list =", result_list)

