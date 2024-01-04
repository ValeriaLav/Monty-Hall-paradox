import random


def without_change(choices):
    # в начале каждой попытки случайно перемешаем массив
    random.shuffle(choices)
    return choices[random.randrange(len(choices))]


def with_change(choices):
    # в начале каждой попытки случайно перемешаем массив
    random.shuffle(choices)
    # первый выбор
    first_choice = random.randrange(len(choices))
    # ведущий открывает дверь с самокатом
    for i in range(len(choices)):
        if i != first_choice and choices[i] == 'samokat':
            master_choice = i
            break
    # делаем второй выбор, меняя первое решение
    for i in range(len(choices)):
        if i != first_choice and i != master_choice:
            return choices[i]


doors = ['samokat', 'samokat', 'avtomobil']
win_count = 0
N = 100000
for _ in range(N):
    result = without_change(doors)
    if result == 'avtomobil':
        win_count += 1
print('Число побед БЕЗ изменения вбора : ', win_count, 'в процентах : ', win_count/N)

win_count = 0
for _ in range(N):
    result = with_change(doors)
    if result == 'avtomobil':
        win_count += 1

print('Число побед С изменением вбора : ', win_count, 'в процентах : ', win_count/N)





