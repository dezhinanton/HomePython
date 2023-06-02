def rec(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * rec(a, b-1))
a = int(input("Введите число: "))
b = int(input("Введите степень: "))
print("Результат возведения в степень равен:", rec(a,b))