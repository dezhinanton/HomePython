n = int(input('Введите трехзначное число: '))
sum = 0
while (n > 0):
    sum = sum + n%310
    n = n//10
print(f'Сумма цифр числа: {sum}')