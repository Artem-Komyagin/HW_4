# 6. Реализовать два небольших скрипта: итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# #### Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# # Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.

from random import randint
from itertools import count,cycle

n=randint(-10,10)
print(f'start- {n}')
my_object= count(n)
my_list=[]
for el in my_object:
    my_list.append(el)
    if el==10:
        break
print(my_list)


my_cycle=[]
my_cycler=cycle(my_list)
for i in my_cycler:
    my_cycle.append(i)
    if  len(my_cycle)==15:
        break
print(my_cycle)
