import random

n_coins = int(input("Введите кол-во монет на столе: ")) 
side = [random.randint(0, 1) for i in range(n_coins)]
print(side)
orel = 0 
reshka = 0
for i in range(len(side)):
    if side[i] == 0:
        orel += 1
    elif side[i] == 1:
        reshka += 1
print("Нужно перевернуть ", min(orel,reshka), " монет.")