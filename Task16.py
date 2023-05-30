n = int(input("Укажите размер массива: ")) 
print("Введите элементы массива:")
arr = [int(input()) for i in range(n)] 
x = int(input("Укажите число x для поиска: ")) 
sum = 0
for i in arr:         
    if i == x:
        sum += 1
    i += 1
print(sum)