from random import randint

def avg(value):
    return sum(value) / len(value)


bal_wawe1 = avg([randint(78, 85) for i in range(100)])#определение проходного балла первой волны
bal_wave2 = avg([randint(70, 85) for i in range(100)])#определение проходного балла второй волны
value_N = randint(60, 100)#определение баллов абитурьента

def start(claim):
    print(f"Приём в ВУЗ открыт\nДокументы поданы\nПроходной балл для 1 волны: {bal_wawe1}\nПроходной балл для 2 "
    f"волны: {bal_wave2}")
    claim['state'] = 'analyzeFirstWave'

def analyzeFirstWave(claim):
    print(f"Результат вступительных испытаний: {value_N}\nКонкурс 1 волна")
    if value_N > bal_wawe1:
        print("Попадание в 1 волну")
        claim['state'] = 'processing'
    else:
        claim['state'] = 'analyzeSecondWave'

def analyzeSecondWave(claim):
    print("Конкурс 2 волна")
    if value_N > bal_wave2:
        print("Попадание в 2 волну")
        claim['state'] = 'processing'
    else:
        print("Конкурс не пройден")
        claim['state'] = 'close'

def processing(claim):
    print("Приказ о зачислении")
    claim['state'] = 'close'

def close(claim):
    print("Приём в ВУЗ закрыт")
    claim['state'] = None

state = {'start': start, 'analyzeFirstWave': analyzeFirstWave, 'analyzeSecondWave': analyzeSecondWave,
'processing': processing, 'close': close}#словарь для перехода по состояниям

def run():#метод последовательного старта
    claim = {'state': 'start'}
    while claim['state'] is not None:
        status = state[claim['state']]
        status(claim)

run()