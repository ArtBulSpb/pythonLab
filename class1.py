import random

class quadrate:

    def perimeter(self, a):
        print("периметр = ", a*4, "\n")

    def square(self, a):
        print("площадь = ", a*a, "\n")


quad1 = quadrate()
quad2 = quadrate()

try:
    i = int(input("введите длину стороны квадрата "))
except:
    i = random.randint(1, 100)
    print("число введено неверно, использовано рандомное значение ", i)

print("Вызываем метод perimeter")
quad1.perimeter(i)  # Hello work

print("Вызываем методы perimeter и square")
quad2.square(i)
quad2.perimeter(i)


