
list_numbers = [2, -5, 8, 9, -25, 25, 4]
list_numbers_new = []
for number in list_numbers:
    if number >= 0:
        number = number ** .5
        if number == int(number):
            list_numbers_new.append(int(number))
print(list_numbers_new)


