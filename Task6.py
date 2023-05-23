n = int(input('Введите шестизначный номер билета: '))
sum = 0
while (n > 0):
    if (n > 1000):
        sum = sum + n%10
        n = n//10
    else:
        sum = sum - n%10
        n = n//10
if (sum == 0):
    print('Счастливый билет')
else:
    print('Обычный билет')