from random import randint
n = int(input("Укажите размер массива: "))
arr = []
for i in range(n):
    arr.append(randint(0, 10))
print(arr)
x = int(input("Укажите число x для поиска: "))
diff = abs(x - arr[0])
for i in range(1, len(arr)):
    if abs(x - arr[i]) <= diff:
        diff = abs(x - arr[i])
        res = arr[i]
print(f"Самый близкий к ч элемент: {res}")