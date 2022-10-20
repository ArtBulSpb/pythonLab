from datetime import date
import random

now = date.today()
study_time = 5


class human:

    def namechange(self):  # метод создания имени
        name = input("Введите имя ")
        if name == "":
            name = "artur"
            print("оставлено стандартное имя ", name)
        else:
            print("Здравствуйте, ", name, "!\n")
        return name

    def yearchange(self):  # метод определения возраста
        # def first(year):
        #     return int(year)
        # def second( newyear):
        #     return int(newyear)

        year = int(now.year) + 1

        while year > now.year:
            try:
                year = int(input(("Введите год рождения. Он должеть быть меньше, чем " + str(now.year) + " ")))

            except:
                year = 2005
                print("год рождения введен неверно, подставлено стандертное значение ", year)
            newyear = " "


            # first(year)
            while (newyear == " "):
                try:
                    newyear = int(input("Введите год, в котором хотите узнать возраст человека  "))
                except:
                    print("год введен неверно ")

            while (newyear < year):
                print("в этом году человек еще не родился ")
                try:
                    newyear = int(input("Введите год, в котором хотите узнать возраст человека  "))
                except:
                    print("год введен неверно ")
        print("43 NY = ", newyear)


        # second(newyear)
        return  int(year), int(newyear)



    def agecount(self, newyear, year):
        age = newyear - year
        print("Возраст в ", newyear, "году будет ", age)
        return age

class student(human):
    def __init__(self, age, newyear):
        self.age = age
        self.newyear = newyear
        # print("init, age = ", age)

    def study(self):
        start_course = 0
        # if self.age >= 17 and self.age <= 27:  # and self.age <= 22:
        #
        #
        # else:

        if self.age < 17:
            print(self.age)
            start_course = 17 - self.age
            print(start_course)
        return start_course
    def course(self, start_course):
        for i in range (start_course, start_course + study_time - 2):
            print("год обучения", i + 1 + self.newyear)



info = human()  # Создаём экземпляр класса
name = info.namechange()  # Вызываем метод класса human()

info2 = student(info.yearchange()[0], info.yearchange()[1])

info2.study()

print("Поздравляем, ", name)
print("Вы зачислены в группу ", random.randint(100, 200))# Назначение группы обучения
print("Начало курса: ", now.year + info2.study()) # Начало занятий
info2.course(now.year + info2.study())
print("Окончание курса: ", now.year + info2.study() + study_time - 1) #Окончание занятий



