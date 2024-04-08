start_sum = int(input())
percent = int(input())
target_sum = int(input())
month_count = 0

while start_sum < target_sum:
    start_sum += start_sum * percent / 100
    month_count += 1
    print(f'{month_count} - {start_sum}')

print(f'Кол-во месяцев: {month_count}')
print(f'Итоговая сумма: {start_sum}')