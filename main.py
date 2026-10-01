import math
x = float(input("ведите х:"))
if x < 4:
    print("Ошибка: х должен быть >= 4")
else:
    y = (-2 * math.sqrt(x-4) * math.tan(math.pi)) / (math.pi ** x)
    print ("у =",y)
if y > 0:
    print ("Положительтное")
    b = y % 2
    if b != 0:
        print("Четное")
    elif b == 0:
        print("Нечетное")
elif y < 0:
    print ("Отрицательное")
    b = y % 2
    if b != 0:
        print("Четное")
    elif b == 0:
        print("Нечетное")
else:
    print("Равно нулю")
    print("Ни четная, ни нечетная")
