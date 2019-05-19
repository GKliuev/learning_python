# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    '''
    возвращает ряд фибоначчи
    от n до m включительно
    '''
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    # разобраться как работает строчка
    res = [fib[i] for i in range(n, m)]
    del fib
    return res


print(fibonacci(5, 10))

# teacher's solution
# def fibonacci(n, m):
#     res = []
#     a_num = 0
#     b_num = 1
#
#     for i in range(m + 1):
#         if i >= n:
#             res.append(b_num)
#         a_num, b_num = b_num, b_num + a_num
#     return res
#
#
# print(fibonacci(5, 10))

# разложить ряд фибоначи:
# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#         # First Fibonacci number is 0
#     elif n == 0:
#         return 0
#     # Second Fibonacci number is 1
#     elif n == 1:
#         return 1
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2)
#
#     # Driver Program
#
#
# print(Fibonacci(9))