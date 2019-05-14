def lucky_ticket(numbers):
    numbers = str(numbers)
    a = sum(map(int, numbers[:3]))
    b = sum(map(int, numbers[3:]))
    if a == b:
        return True
    return False


x = lucky_ticket(123123)
print(x)

