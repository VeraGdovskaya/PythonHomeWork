# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

N = int(input('input N: '))
factor = []
i = 2
while  i <= N:
    if N % i == 0 :
       factor.append(i)
       N = N / i
    else:
      i +=1
print(factor)   
 

# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

data = list(map(int, input('введите числа через пробел: ').split()))
res = []
for i in data:
    if i not in res:
        res.append(i)

print(f'{data} -> {res}')

# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4



list_student=[]
with open('marks.txt','r', encoding = 'utf-8') as data:
    for line in data:
        if '5' in line:
            line = line.upper()
            list_student.append(line.replace('\n', ' '))
print(list_student)
  
  
  
#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


def Ceacer_chiper():
    
    alfabet_eng = 'abcdefghijklpnomqrstuvwxyzabcdefghijklpnomqrstuvwxyz'
    # alfabet_ru = "абвгдежзежзийуклмнопрстуфхцчшщъыйэюяабвгдежзежзийуклмнопрстуфхцчшщъыйэюя"
    message = input('Please enter a massage need to be encrypted: ')
    key = int(input('Please eenter a key (number from 1 to 26): '))
    message = message.lower()
    encrypted = ''
    for letter in message:
        position = alfabet_eng.find(letter)
        # position = alfabet_ru.find(letter)
        new_position = position + key
        if letter in alfabet_eng:
            encrypted = encrypted + alfabet_eng[new_position] 
        # elif letter in alfabet_ru:
            # encrypted = encrypted + alfabet_ru[new_position]
        else:
            encrypted = encrypted + letter # если в сообщении содержится цифра, знак пунктуации или др символ не из алфавита
    
    print (encrypted)      

encrypted = Ceacer_chiper()
    

def De_Ceacer_chiper():
    alfabet_eng = 'abcdefghijklpnomqrstuvwxyzabcdefghijklpnomqrstuvwxyz'
    #alfabet_ru = "абвгдежзежзийуклмнопрстуфхцчшщъыйэюяабвгдежзежзийуклмнопрстуфхцчшщъыйэюя"
    enrcepted_message = input('Please enter a massage need to be de-encrypted: ')
    key = int(input('Please eenter a key (number from 1 to 26): '))
    enrcepted_message = enrcepted_message.lower()
    de_encrypted = ''
    for letter in enrcepted_message:
        position = alfabet_eng.find(letter)
        #position = alfabet_ru.find(letter)
        new_position = position - key
        if letter in alfabet_eng:
            de_encrypted = de_encrypted + alfabet_eng[new_position] 
       # elif letter in alfabet_ru:
            # de_encrypted = de_encrypted + alfabet_ru[new_position]
        else:
            de_encrypted = de_encrypted + letter # если в сообщении содержится цифра, знак пунктуации или др символ не из алфавита
    
    print(de_encrypted)
       

de_encrypted = De_Ceacer_chiper()


#  5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# 
# файл второй:
# сжатый текст

# data = open('book1.txt' , 'w', encoding = 'utf-8')
# data.write ('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')

def rle_coding(data):
    res =''
    count = 1

    for i in range(len(data)-1):
        if data[i] == data[i+1]:
            count +=1
        else:
            res = res + str(count)+ data[i]
            count = 1
    if count > 1 or (data[len(data)-2] != data[len(data)-1]):
        res = res + str(count)+ data[-1]
    # print(res)
    return res
        
# def rle_decoding(data2):
#     number =''
#     res2 = ''
#     for i in range(len(data2)):
#         if not data[i].isalpha:
#             number+=data2[i]
#         else:
#             res2 = res2 +data2[i]* int(number)
#             number = ''
#     print(res2)
#     return res2

data = input("Введите текст для кодировки: ")
# data2 = input("Введите текст для раскодировки: ")
print(f"{data} -> {rle_coding(data)}")
# print(f"Текст после дешифровки: {rle_decoding(data2)}")
