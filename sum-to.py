# Дано целое положительное.
# Дана последовательность из целых положительных
# Записать в выходной файл "1", если
# в последовательности есть два числа сумма, которых равна
# значению "target" или "0" если таких нет.

from datetime import datetime
import time

start_time = datetime.now()

# data_list = []  # список взодных значений
res_list = []  # список значение переведенныый int
target = 0  # исходное число, по которому ищем слагаемые
mediana = 0  # значения списка больше этого значения не обрабатывать
# это  target деленое на 2

res = 0
file = open("input.txt", "r")

line = file.readline()
target = int(line)
mediana = target // 2
check = bool(target % 2)
line = file.readline()
file.close()

data_list = line.split()
data_list = sorted(data_list)  # сортируем список по возрастанию
for i in data_list:
    if target < int(i):
        break  # ограничиваем список значением target
    res_list.append(int(i))  # создаем преобразованный список

#  при рчередном  значении проверяем, есть ли в списке значение,
#  дополняющее до значение target. Если есть,, цель достигнута



for i in res_list:
    n = target - i
    if n in res_list:
        if target != 1:
            if i > mediana:
                break
            elif (i == mediana) and (not check):
                if res_list.count(i) == 1:
                    break
        res = 1



file = open("output.txt", "w")
file.write(str(res) + '\n')
file.close()

print(datetime.now() - start_time)

