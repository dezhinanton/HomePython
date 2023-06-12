min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))
indexes = []
import random
num = 12
new_list = [random.randint(0, 10) for i in range(num)]
print(new_list)
for i in range(len(new_list)):
    if new_list[i] >= min_value and new_list[i] <= max_value:
        indexes.append(i)
print("Индексы элементов, удовлетворяющих условия:", indexes)