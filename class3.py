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
            newyear = " "

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

        return int(year), int(newyear)

    def agecount(self, year):
        age = now.year - year
        print("Сейчас Вам ", age, " лет.")
        return age
    def futureAgecount(self, newyear, year):
        fage = newyear - year
        print("В ", newyear, "году вам стукнет ", fage, "лет.")
        return fage

class student(human):
    def __init__(self, age, newyear):
        self.age = age
        self.newyear = newyear

    def study(self):
        start_course = 0
        # if self.age >= 17 and self.age <= 27:  # and self.age <= 22:
        #
        #
        # else:

        if self.age < 17:
            #print("self.age = ", self.age)
            start_course = 17 - self.age
        #print("start_course = ", start_course)
        return start_course

    def course(self, start_course):
        for i in range(start_course+1, start_course + study_time - 1):
            print("год обучения", i)


info = human()  # Создаём экземпляр класса
name = info.namechange()  # Вызываем метод класса human()
middle = info.yearchange()
age_count = info.agecount(middle[0])
future_age = info.futureAgecount(middle[1], middle[0])
info2 = student(age_count, middle[1])

start_course = info2.study()

start_study = now.year + start_course

print("Поздравляем, ", name)
print("Вы зачислены в группу ", random.randint(100, 200), "\n")  # Назначение группы обучения
print("Начало обчения: ", now.year + start_course)  # Начало занятий
info2.course(start_study) #распечатка по годам
print("Окончание курса: ", start_study + study_time - 1)  # Окончание занятий
print("\nСтоимость обучения в ГУАП составляет 46 000руб./сессия. Скидок нет.")
