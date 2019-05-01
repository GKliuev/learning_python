list_fruits = ["яблоко", "банан", "киви", "арбуз"]
i = 0
for fruit in list_fruits:
    i += 1
    print(str(i) + '.', fruit.rjust(10))
