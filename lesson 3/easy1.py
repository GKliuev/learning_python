import math


def my_round(number, digits):
  multiplier = pow(10.0, digits) # pow(x**y)
  return int(number*multiplier + 0.5) / multiplier


number = float(input('Введите число'))
ndigits = int(input('Введите количетсво знаков после запятой'))
print(my_round(number, ndigits))