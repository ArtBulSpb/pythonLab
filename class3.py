class human:
    def namechange(self): #метод создания имени
        name = input("введите имя ")
        if name == "":
            name = "artur"
            print("оставлено стандартное имя ", name)
        else:
            print("Имя изменено на " + name)
    def yearchange(self):#метод определения возраста
        while True:
            try:
                year = int(input("введите год рождения "))
            except:
                year = 2005
                print("год рождения введен неверно, подставлено стандертное значение ", year)
            try:
                newyear = int(input("введите год, возраст человека в котором хотите узнать "))
            except:
                newyear = 2022

            old = newyear - year
            print("возраст = ", old)
            break
class student(human):
    name = human.namechange()#наследование имени
    old = human.yearchange()#наследование возраста

    def name2(self):
        print(name)
info = human()
info.namechange()#использование методов
info.yearchange()#использование методов
info2 = student
info2.name2()#использование методов






