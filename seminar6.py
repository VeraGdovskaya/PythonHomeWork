# 1- Определить, присутствует ли в заданном списке строк, некоторое число

data = ('jgh kghf dhg dfgkh rhjg dfgh ').split()
n = str(input('введите символ который нужно найти: '))
result = len(list(filter(lambda x: n in x, data)))
print(f'наш список {data}, ищем {n} -> {result} ')
    


# 2- Найти сумму чисел списка стоящих на нечетной позиции


numbers = input('введите числа ').split()
data = list(map(int, numbers))
sum_elem = sum(data[1::2]) 
print(sum_elem)

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from math import sqrt

x1 = int(input('введите координату x точки A '))
y1 = int(input('введите координату y точки A '))
x2 = int(input('введите координату x точки B '))
y2 = int(input('введите координату y точки B ')) 

result = round(float(sqrt((x2-x1)**2+(y2-y1)**2)), 2) 
result = round(result, 2) 
print(f'A({x1},{y1}); B({x2},{y2}) -> {result}')    

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

data = ('йцу фыв ячс цук йцу кен йцу ').split()
n = str(input('введите символ который нужно найти: '))
result = len(list(filter(lambda x: n in x, data)))
print(f'наш список {data}, ищем {n} -> {result} ')

# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

my_list = [2, 3, 4, 5]
result_list =[]
for i in range((len(my_list)+1)//2):
    result_list.append(my_list[i]*my_list[len(my_list)-1-i])
print(result_list)

# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = 5
fibo_list = [(-3)**i for i in range(0, N)]
print(fibo_list)