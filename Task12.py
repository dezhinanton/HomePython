x = 10
y = 10
p = x*y
s = x+y
input_x = int(input("Отгадайте первое число: "))
input_y = int(input("Отгадайте второе число: "))
if x*y == input_x*input_y and x+y == input_x+input_y:
    print("Вы отгадали числа! Сумма = ", input_x+input_y, ", произведение = ",input_y*input_x)
else: 
    print("Попробуйте ещё!")