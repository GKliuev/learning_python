import random

# my solution
# def random_number_list(n, range_min, range_max):
#     list_random = []
#     i = 0
#     while i < n:
#         rand = random.randint(range_min, range_max)
#         list_random.append(rand)
#         i += 1
#     return list_random

# teacher's solution

def random_number_list(n, range_min, range_max):
    list_random = []
    for _ in range (n):
        list_random.append(random.randint(range_min, range_max))
    return list_random


elem_count = int(input('Введите целое число: '))
list_random = random_number_list(elem_count, -100, 100)
print(list_random)
