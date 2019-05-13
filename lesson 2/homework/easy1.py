# my solution
# list_fruits = ["яблоко", "банан", "киви", "арбуз"]
# i = 0
# for fruit in list_fruits:
#     i += 1
#     print(str(i) + '.', fruit.rjust(10))

# teacher's solution
list_fruits = ["яблоко", "банан", "киви", "арбуз"]
right_offset = len(max(list_fruits, key=len))
for index, item in enumerate(list_fruits, start=1):
    print('{}. {}'.format(index, item.rjust(right_offset)))

