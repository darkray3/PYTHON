number = int(input('Введите число: '))
summ = 0
while number > 0:
    summ += number % 10
    number //= 10
print(f'Сумма цифр числа равна {summ}')