import random

class quadrate:

    def perimeter(self, a):
        print("периметр = ", a*4, "\n")

    def square(self, a):
        print("площадь = ", a*a, "\n")

    def request(self):
        try:
            i = int(input("введите длину стороны квадрата "))
        except:
            i = random.randint(1, 100)
            print("число введено неверно, использовано рандомное значение ", i)
        return i

quad1 = quadrate()
quad2 = quadrate()


print("Вызываем метод perimeter")
quad1.perimeter(quad1.request())  # Hello work

print("Вызываем методы perimeter и square")
quad2.square(quad1.request())
quad2.perimeter(quad1.request())


