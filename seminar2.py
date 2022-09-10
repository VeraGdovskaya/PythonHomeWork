# ДЗ

# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 

# Пример:
# 67.82 -> 23
# 0.56 -> 11

num = (input('введите вещественное число '))
num2 = list(num)  # делаю список
   
for i in num2:
   if i == "." or i == "-":
    num2.remove(i) # удаляю точку
   
for i in range(len(num2)):
    num2[i] = int(num2[i])  # именяю троки на числа
       
print(f'{num} -> {sum(num2)}')




# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('введите число '))

array = []   

def result (array, N):
    count = 0
    P = 1
    while (count <= N):
        count += 1
        P *= count 
        array.append(P)  
    print(array)

result(array,N)

#  3. Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

num = input('enter number: ')
poli1=num
poli2=None
while True:
   poli2 = "".join(reversed(poli1))
   if poli1 == poli2:
      print("polindrom has been found:", poli2)
      break
   else:
      p = int(poli1) + int(poli2)
      poli1 = str(p)
      
#  или  

def polindrom_number(num):
   rev_num = str(num)[::-1]
   if str(num) == str(rev_num):
      return num
   return polindrom_number(int(rev_num)+ num)

print(polindrom_number(67))
      


# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)
# Домашнее задание отправляйте в виде ссылки на гит-репозиторий

import datetime
import math

def find_number(min, max):
   d = max - min
   ms = datetime.datetime.today().microsecond/(10**6)
   print(ms)
   return min + math.ceil(d*ms)


print(find_number(10, 70))