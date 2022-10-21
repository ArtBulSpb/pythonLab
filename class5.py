import random

valuelist = ["евро ", "доллар ", "тенге ", "юань ", "лира "]


class exchange:
    # def __init__(self, exchange_rate = 1):
    #     self.exchange_rate = []
    def market(self):
        counter = 0
        exchange_rate = []
        value = input("введите желаемою валюту ")
        datecounter = 0
        exchange_rate_min = 0
        if value == "":
            value = random.choice(valuelist)
            print("выбрана валюта ", value)
        while datecounter <= 6:
            datecounter = datecounter + 1


            try:
                a = int(input("введите курс в рублях "))
            except:
                print("курс введен неправильно ")
                break
            if a > 0:
                exchange_rate.append(a)
                if datecounter == 1:
                    exchange_rate_min = a
                    # print("25 a =  ", a)
                    # print("26 exchange_rate_min=  ", exchange_rate_min)
                    # print("27 counter=  ", counter)
                else:
                    if a < exchange_rate_min:
                        print("a =  ", a)
                        exchange_rate_min = a
                        # print("32 exchange_rate_min=  ", exchange_rate_min)
                        counter = datecounter
                        # print("34 counter=  ", counter)
                print("день ", datecounter, exchange_rate)
            else:
                print("курс не может быть отрицательным ")
                break
        if counter != 0:
            print("минимальный курс ", value, "= ", exchange_rate_min, " в ", counter, " день")
        else:
            print("минимальный курс ", value, "= ", exchange_rate_min, "руб   в ", counter + 1, " день")


print("Объект 1 ")
a = exchange()
a.market()

print("Объект 2 ")
b = exchange()
b.market()
