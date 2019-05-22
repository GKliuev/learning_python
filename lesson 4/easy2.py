# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

first_fruits_list = ["яблоко", "киви", "арбуз"]
second_fruits_list = ["банан", "киви", "арбуз"]
# result_fruits_list = [el for el in first_fruits_list if el in second_fruits_list]
result_fruits_list = []
for el in first_fruits_list:
    if el in second_fruits_list:
        result_fruits_list.append(el)

print('Result fruits list =', result_fruits_list)