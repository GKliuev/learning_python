list_numbers = [20, 42, 11, 13, 101, 250, 14]
list_numbers_new = []
for number in list_numbers:
    if number % 2 == 0:
        list_numbers_new.append(number / 4)
    else:
        list_numbers_new.append(number * 2)
print(list_numbers_new)
