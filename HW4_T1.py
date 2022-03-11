# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
#
from sys import argv
script,t,r,p=argv
print('script: ', script)
print('time: ', t)
print('Rate: ', r)
print('prize: ', p)
def sal():
     t=int(argv[1]) * int(argv[2]) + int(argv[3])
     return f'Your Salary is {t}'
print(sal())