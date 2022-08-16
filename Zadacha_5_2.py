import random


def game_vs_player():
    konfeti = 202
    print('Количество конфет на столе: ', konfeti)
    while konfeti > 1:
        print('Ход первого игрока!')
        while True:
            first_player = int(input('Введите число конфет, которое хотите взять: '))
            if first_player < 29:
                konfeti -= first_player
                print('Осталось конфет на столе:', konfeti)
                print()
                break
            else:
                print('Нельзя взять больше 28 конфет! Попробуй ещё раз')
        if konfeti < 1:
            print('Первый игрок победил!')
            break
        print('Ход второго игрока!')
        while True:
            second_player = int(input('Введите число конфет, которое хотите взять: '))
            if second_player < 29:
                konfeti -= second_player
                print('Осталось конфет на столе:', konfeti)
                print()
                break
            else:
                print('Нельзя взять больше 28 конфет! Попробуй ещё раз')


def game_vs_bot():
    konfeti = 202
    print('Количество конфет на столе: ', konfeti)
    while konfeti > 1:
        print('Ваш ход!')
        while True:
            first_player = int(input('Введите число конфет, которое хотите взять: '))
            if first_player < 29:
                konfeti -= first_player
                if konfeti < 1:
                    print('Вы победили! Поздравляем!')
                    break
                print('Осталось конфет на столе:', konfeti)
                print()
                break
            else:
                print('Нельзя взять больше 28 конфет! Попробуй ещё раз')
        second_player = random.randint(1,28)
        if konfeti < 29:
            second_player = konfeti
        konfeti -= second_player
        print('Ход вашего противника!')
        print('Противник взял конфет: ',second_player)
        print('Осталось конфет на столе:', konfeti)
        if konfeti < 1:
            print('Кажется ... вы проиграли.')
            break
        print()




print('Добро пожаловать в игру!')
print('Для игры против бота - введите 1')
print('Для игры против другого человека - введите 2')
while True:
    choice = int(input('Выберите режим: '))
    if choice == 1:
        print('Вы выбрали игру против бота! Начинаем!')
        break
    elif choice == 2:
        print('Вы выбрали игру против другого человека! Начинаем!')
        break
    else:
        print('Такого режима нет, попробуйте ещё раз!')

print()
if choice == 2:
    game_vs_player()
elif choice == 1:
    game_vs_bot()


print('Игра окончена!')
