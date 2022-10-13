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

        year = int(now.year) + 1

        while year > now.year:
            try:
                year = int(input(("Введите год рождения. Он должеть быть меньше, чем " + str(now.year) + " ")))

            except:
                year = 2005
                print("год рождения введен неверно, подставлено стандертное значение ", year)

        try:
            # TODO Обработать ввод года меньше года рождения
            newyear = int(input("Введите год, в котором хотите узнать возраст человека  "))
        except:
            newyear = 2022

        age = newyear - year
        print("Возраст в ", newyear, "году будет ", age)
        return age


class student(human):
    def __init__(self, age):
        self.age = age
        # print("init, age = ", age)

    def study(self):

        if self.age >= 17:  # and self.age <= 22:
            start_course = 0

        else:

            if self.age < 17:
                start_course = 17 - self.age

        return start_course


info = human()  # Создаём экземпляр класса
name = info.namechange()  # Вызываем метод класса human()

info2 = student(info.yearchange())
info2.study()
print("Поздравляем, ", name)
print("Вы зачислены в группу ", random.randint(100, 200))# Назначение группы обучения
print("Начало курса: ", now.year + info2.study()) # Начало занятий
print("Окончание курса: ", now.year + info2.study() + study_time) #Окончание занятий

