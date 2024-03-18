mushroom = int(input('Введите количество грибов: '))
if mushroom % 100 >= 11 and mushroom % 100 <= 14:
    print('грибов')
elif mushroom % 10 >= 2 and mushroom % 10 <= 4:
    print('гриба')
elif mushroom % 10 == 1:
    print('гриб')
else:
    print('грибов')