# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"


# def del_text(data):
#     for i in data:
#         if not 'абв' in i:
#             res = res + i
#     return res

# res = (del_text('абвгдейка - это передача'))
   
# print (res)

    
data = 'абвгдейка - это передача'
data2 = data.split()
res = ''
for i in data2:
    if not 'абв' in i:
        res = res + ' ' + i 
print(f'{data} -> {res}')


# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# import random
# from random import randint, choice
 
print(
    '"Игра с конфетами"\n'
    'В игре участвуют два игрока\n'
    'Первый ход определяется жеребьевкой.\n'
    'Игроки ходят, совершая ход друг после друга\n'
    'Правила игры\n'
    'У нас есть некоторое количество конфет\n'
    'За один ход можно забрать не более определенного количества конфет, о котором мы договоримся\n'
    'Тот, кому достанется последняя конфета - проиграл\n'
    )
 
messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
            'сколько конфет берем?', 'берите еще', 'Ваш ход']
max_number_move = 0
 
def introduce_players():
    player1 = input('Первый игрок, представьтесь\n')
    player2 = 'SmartBOT'
    print(f'Очень приятно, сегодня Вы играете с искуственным  {player2}')
    return [player1, player2]
 
def sweets_game(players):
    global max_number_move
    total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
    max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [total_sweets, max_number_move, int(first)]
 
max_move = max_number_move
 
def game_player_vs_smart_bot(sweets, players, messages):
    global max_number_move
    count = sweets[2]
 
 
    while sweets[0] > 0:
        if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
            move = sweets[0] -1
            print(f'Я забираю {move}')
 
        elif not count % 2:
            move = random.randint(1, sweets[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > sweets[0] or move > sweets[1]:
                print(
                    f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                chance = 2
                while chance > 0:
                    if sweets[0] >= move <= sweets[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                    move = int(input())
                    chance -= 1
                else:
                    return print(f'Попыток не осталось. Game over!')
        sweets[0] = sweets[0] - move
        if sweets[0] > 0:
            print(f'Осталось {sweets[0]} конфет')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]
 
 
players = introduce_players()
sweets = sweets_game(players)
 
winer = game_player_vs_smart_bot(sweets, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

languege = 'PYTHON c# java'.split()
languege = [i.upper() for i in languege]
num = [i for i in range(1, len(languege)+1)]
res = list(zip(num, languege))
print(res)
