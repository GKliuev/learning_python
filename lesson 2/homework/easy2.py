list1 = [1, 2, 3, 4, 5, 4, 7, 8, 9]
list2 = [3, 4, 5, 6, 7]

# в этом варианте всегда остаётся 4 в обоих списках - необходимо было добавить .copy  к спискам
# for number1 in list1.copy():
#     for number2 in list2.copy():
#         if number1 == number2:
#             list1.remove(number1)
# print(list1)


# делаем новый список с непересикающимися элемантами
# result = list(set(list1) ^ set(list2))
# print(result)

# создаём новые списки и вычитаем списки друг из друга
# list1_new = list(set(list1) - set(list2))
# list2_new = list(set(list2) - set(list1))
#
# print(list1_new, list2_new)

# тут можно посмотреть как делать сравнение списков
# https://ru.stackoverflow.com/questions/427942/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5-2-%D1%83%D1%85-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%BE%D0%B2-%D0%B2-python

# teacher's solution
# for number in list2:
#     while number in list1:
#         list1.remove(number)
# print(list1)
