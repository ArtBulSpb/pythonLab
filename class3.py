from datetime import date

now = date.today()


class human:
    def namechange(self):  # метод создания имени
        name = input("введите имя ")
        if name == "":
            name = "artur"
            print("оставлено стандартное имя ", name)
        else:
            print("Имя изменено на " + name, "\n", "Здравствуйте, ", name, "!\n")
        return name

    def yearchange(self):  # метод определения возраста

        while True:
            year = int(now.year) + 1
            print(year)

            while year > now.year:
                try:
                    print("try")
                    year = int(input(("введите год рождения. Он должеть быть меньше, чем " + str(now.year) + " ")))

                except:
                    year = 2005
                    print("год рождения введен неверно, подставлено стандертное значение ", year)

            try:
                newyear = int(input("введите год, в котором хотите узнать возраст человека  "))
            except:
                newyear = 2022

            age = newyear - year
            print("возраст = ", age)
            break


class student(human):
    def study(self, old):
        for old in range(17, 22):
            kyrc = kyrc + 1
            print("курс ", kyrc)


info = human()
info.namechange()  # использование методов
info.yearchange()  # использование методов
