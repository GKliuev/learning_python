# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
if __name__ == '__main__':
    print("Задача 1: \n")
import os


def make_dir(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('{} - уже существует'.format(name))


def remove_dir(name):
    try:
        os.removedirs(name)
    except FileNotFoundError:
        print('{} - папки не существует'.format(name))


def start():
    answer = ''
    quantity_dirs = range(1, 10)

    while answer != '3':

        answer = input('Выберите пункт меню:\n'
                       '1. Создать папки dir_1 - dir_9\n'
                       '2. Удалить папки dir_1 - dir_9\n'
                       '3. Выход\n')
        if answer == '3':
            break
        if answer == '1':
            print("Папки созданы\n")
            for i in quantity_dirs:
                i = str(i)
                make_dir('dir_' + i)
        elif answer == '2':
            print("Папки удалены\n")
            for i in quantity_dirs:
                i = str(i)
                remove_dir('dir_' + i)


if __name__ == '__main__':
    start()

print()
print(30 * "-")
print()