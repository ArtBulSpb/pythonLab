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
        return name

    def yearchange(self):  # метод определения возраста
        global year
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
        print("В ", newyear, "году  ", fage, "лет.")
        return fage

class student(human):
    def __init__(self, age, newyear):
        self.age = age
        self.newyear = newyear

    def study(self):
        start_course = 0
        if self.age < 17:
            start_course = 17 - self.age
        return start_course

    def course(self, start_course, trigger):
        random.seed(version=2)
        if trigger:
            time_data = start_course + study_time - 1
        else:
            time_data = start_course + random.randint(1, study_time) - 1
        for i in range(start_course + 1, time_data):
            print("год обучения", i)
        if not trigger:
            print("студент отчислен ")


#student1
print("student1")
info = human()  # Создаём экземпляр класса
name = info.namechange()  # Вызываем метод класса human()
middle = info.yearchange() # возвращает кортеж из год рождения и год в котором нужно узнать возраст
age_count = info.agecount(middle[0])
future_age = info.futureAgecount(middle[1], middle[0])
info2 = student(age_count, middle[1])

start_course = info2.study()
start_study = now.year + start_course

print("Поздравляем, ", name)
print("Вы зачислены в группу ", random.randint(100, 200), "\n")  # Назначение группы обучения
print("Начало обчения: ", year + 17 )  # Начало занятий
info2.course((year + 17), 1) #распечатка по годам
print("Окончание курса: ", year + 17 + study_time - 1)  # Окончание занятий
print("\nСтоимость обучения в ГУАП составляет 46 000руб./сессия. Скидок нет.\n\n")

#student2
print("student1")
info3 = human()  # Создаём экземпляр класса
name1 = info3.namechange()  # Вызываем метод класса human()
middle1 = info3.yearchange()# возвращает кортеж из год рождения и год в котором нужно узнать возраст
print(middle1, "midl")
age_count1 = info3.agecount(middle1[0])
future_age1 = info3.futureAgecount(middle1[1], middle1[0])
info4 = student(age_count1, middle1[1])

start_course2 = info4.study()
start_study2 = now.year + start_course2

print("Поздравляем, ", name1)
print("Вы зачислены в группу ", random.randint(100, 200), "\n")  # Назначение группы обучения
print("Начало обчения: ", year + 17 )  # Начало занятий
info4.course((year + 17), 0) #распечатка по годам
print("\nСтоимость обучения в ГУАП составляет 46 000руб./сессия. Скидок нет. \n\n")

#student3
print("student1")

info5 = human()  # Создаём экземпляр класса
name3 = info5.namechange()  # Вызываем метод класса human()
middle3 = info5.yearchange() # возвращает кортеж из год рождения и год в котором нужно узнать возраст
age_count3 = info5.agecount(middle3[0])
future_age3 = info5.futureAgecount(middle3[1], middle3[0])
info6 = student(age_count3, middle3[1])

start_course3 = info6.study()
start_study3 = now.year + start_course

print("Поздравляем, ", name3)
print("Вы зачислены в группу ", random.randint(100, 200), "\n")  # Назначение группы обучения
print("Начало обчения: ", year + 17 )  # Начало занятий
info6.course((year + 17), 1) #распечатка по годам
print("Окончание курса: ", year + 17 + study_time - 1)  # Окончание занятий
print("\nСтоимость обучения в ГУАП составляет 46 000руб./сессия. Скидок нет.")
