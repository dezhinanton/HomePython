import random
n = int(input("Введите количество кустов: "))
arr = [random.randint(1, n) for i in range(n)]
print(arr)
i = 0
max = 0
while i < len(arr)-1:
    if max < arr[i-1] + arr[i] + arr[i + 1]:
        max = arr[i-1] + arr[i] + arr[i + 1]
    i+=1
print(max)