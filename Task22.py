from random import randint
n = int(input("Укажите размер массива: "))
arr1 = []
for i in range(n):
    arr1.append(randint(1, 10))
print(arr1)
m = int(input("Укажите размер второго массива: "))
arr2 = []
for i in range(m):
    arr2.append(randint(1, 10))
print(arr2)
all_numbers = list()
for num in arr1:
    if num in arr2:
        all_numbers.append(num)
print(sorted(set(all_numbers)))