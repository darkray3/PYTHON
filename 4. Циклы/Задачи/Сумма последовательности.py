sum_num = 0
while True:
    num = int(input())
    if num == 0:
        break
    sum_num += num
print(sum_num)

"""
Альтернативная версия.
sum_num = 0
while (num := int(input())) != 0:
    sum_num += num
print(sum_num)"""