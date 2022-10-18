from random import randint

def avg(value):
    return sum(value) / len(value)

# fixWaveFirst = 73
# fixWaveSecond = 83

fixWaveFirst = avg([randint(78, 85) for i in range(100)])
fixWaveSecond = avg([randint(70, 85) for i in range(100)])
valueN = randint(60, 100)

def start(claim):
    print(f"Приём в ВУЗ открыт\nДокументы поданы\nПроходной балл для 1 волны: {fixWaveFirst}\nПроходной балл для 2 "
    f"волны: {fixWaveSecond}")
    claim['state'] = 'analyzeFirstWave'

def analyzeFirstWave(claim):
    print(f"Результат вступительных испытаний: {valueN}\nКонкурс 1 волна")
    if valueN > fixWaveFirst:
        print("Попадание в 1 волну")
        claim['state'] = 'processing'
    else:
        claim['state'] = 'analyzeSecondWave'

def analyzeSecondWave(claim):
    print("Конкурс 2 волна")
    if valueN > fixWaveSecond:
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
'processing': processing, 'close': close}

def run_claim():
    claim = {'state': 'start'}
    while claim['state'] is not None:
        fun = state[claim['state']]
        fun(claim)

print("Заявка:\n")
run_claim()