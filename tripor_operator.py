import random

numbers = []
for i in range(10):
    numbers.append(random.randint(a=0, b=100))
print(numbers)

print("Число 13 есть в нашем списке") if 13 in numbers else print("Число 13 нет в нашем списке")

result = None
if 4 in numbers:
    result = 'Есть китайское несчастливое число'
else:
    result = 'Всё окей'
print('Результат выражения:\n', result)

if 7 in numbers:
    result = 'Есть счастливое число'
else:
    result = "Его нету. Вам не повезло"
print('Результат выражения:\n', result)
