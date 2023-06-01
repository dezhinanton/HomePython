import random
n = int(input("Введите количество кустов: "))
arr = [random.randint(1, n) for i in range(n)]
print(arr)
max = 0
for i in range(1, len(arr) - 1):
   if max < arr[i - 1] + arr[i] + arr[i + 1]:
      max = arr[i - 1] + arr[i] + arr[i + 1]
if max < arr[0] + arr[1] + arr[len(arr) - 1]:
   max = arr[0] + arr[1] + arr[len(arr) - 1]
if max < arr[0] + arr[len(arr) - 1] + arr[len(arr) - 2]:
   max = arr[0] + arr[len(arr) - 1] + arr[len(arr) - 2]
print(max)