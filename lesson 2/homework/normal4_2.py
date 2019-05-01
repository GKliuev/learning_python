lst = [1 , 2, 4, 5, 6, 2, 5, 2]

lst_new = []
for i in lst:
    if lst.count(i) == 1:
        lst_new.append(i)

print(lst_new)