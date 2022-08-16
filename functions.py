#2- Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.

import random

def turn_order():
    '''
    Определение первого ходящего.
    '''
    ord = random.randint(1, 2)
    if ord == 1:
        flag = 0
    else:
        flag = 1
    return flag #0 human. 1 bot
   
   
def step(n: int, take_cand: int):
#     '''
#     Только для хуманов!
#     Принимает оставшееся количество конфет, дает сделать ход.
#     Возвращает количество конфет, оставшихся после хода.
#     '''
#     print('Осталось {0} конфет.'.format(n))
#     while True:
#         take = int(input('Введите количество конфет: '))
#         if (take > max_cand):
#             print('Нельзя брать больше {0} конфет за раз!'.format(max_cand))
#             continue
#         elif(take > n):
#             print('Столько конфет не осталось!')
#             continue
#         else:
#             break
    n = n - take_cand
    return n


def bot_step(n: int, max_cand: int):
#     '''
#     Функция просчитывает ход бота.
#     Принимает оставшееся количество конфет, вычисляет количество взятых ботом конфет.
#     Возвращает количество конфет, оставшихся после хода.
#     '''
#     print('Осталось {0} конфет.'.format(n))
    if n == 1:
        take = 1
    elif (n > max_cand):
        take = random.randint(1, max_cand)
    else:
        take = random.randint(1, n)
#     print('Бот берёт {0} конфет.'.format(take))
    n = n - take
    return n, take

   
# def rotation(flag: int, n: int):
#     '''
#     Принимает вспомогательную переменную flag, определяющую ходившего, делает ротацию игроков и вычисляет победившего.
#     Для хуманов!.
#     '''
#     while True:
#         if flag == 0:
#             print('Ходит игрок {0}'.format(flag+1))
#             n = step(n, max_cand)
#             if (n <= 0):
#                 print('Победил игрок 2!')
#                 break
#             flag = 1
#         else:
#             flag = 1
#             print('Ходит игрок {0}'.format(flag+1))
#             n = step(n, max_cand)
#             if (n <= 0):
#                 print('Победил игрок 1!')
#                 break
#             flag = 0


# def with_bot(flag: int, n: int):
#     '''
#     Принимает вспомогательную переменную flag, определяющую ходившего, делает ротацию игроков и вычисляет победившего.
#     Для игры с ботом.
#     '''
#     while True:
#         if flag == 0:
#             print('Сейчас ходит человек')
#             n = step(n, max_cand)
#             if (n <= 0):
#                 print('Победил бот!')
#                 break
#             flag = 1
#         else:
#             flag = 1
#             print('Ходит бот')
#             n = bot_step(n, max_cand)
#             if (n <= 0):
#                 print('Победил человек!')
#                 break
#             flag = 0
           

# candys = 100#2021
# max_cand = 15

# while True:             #Проверка вводимых данных
#     mode = input('Привет! Выберите режим игры: 1 - два игрока, 2 - с ботом: ')
#     if mode.isdigit() == False or int(mode) > 2:
#         print('Введите верные данные!')
#     else:
#         break

# if(mode == '1'):
#     flag = turn_order() #определение кто ходит первым
#     rotation(flag, candys)
# else:
#     flag = turn_order() #определение кто ходит первым
#     with_bot(flag, candys)

