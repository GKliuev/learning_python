import random


def random_number_list(n, range_min, range_max):
    list_random = []
    i = 0
    while i < n:
        rand = random.randint(range_min, range_max)
        list_random.append(rand)
        i += 1
    return list_random


list_random = random_number_list(30, -100, 100)
print(list_random)