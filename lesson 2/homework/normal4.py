lst = [1, 2, 4, 5, 6, 2, 5, 2]


# один из способов
# lst_new = set(lst)

# универсальный метод
lst_new = []
for i in lst:
    if i not in lst_new:
        lst_new.append(i)

print(lst_new)