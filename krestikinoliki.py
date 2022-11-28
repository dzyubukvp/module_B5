# Игра Крестики-нолики для двух игроков
pole = [1,2,3,
        4,5,6,
        7,8,9
        ]

ura_victory = [[0,1,2],
               [3,4,5],
               [6,7,8],
               [0,3,6],
               [1,4,7],
               [3,6,9],
               [0,4,8],
               [2,4,6]
               ]
# рисуем поле битвы
def pole_vidim():
    print(pole[0], end=" ")# 1 линия
    print(pole[1], end=" ")
    print(pole[2])

    print(pole[3], end=" ")  # 2 линия
    print(pole[4], end=" ")
    print(pole[5])

    print(pole[6], end=" ")  # 3 линия
    print(pole[7], end=" ")
    print(pole[8])

#функция обработки события выбора ячейки поля
def napole(step,symbol):
    ind = pole.index(step)
    pole[ind] = symbol


def get_result():
    win = ""

    for i in ura_victory:
        if pole[i[0]] == "X" and pole[i[1]] == "X" and pole[i[2]] == "X":
            win = "X"
        if pole[i[0]] == "O" and pole[i[1]] == "O" and pole[i[2]] == "O":
            win = "O"


    return win


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    pole_vidim()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Ход игрока № 1: "))
    else:
        symbol = "O"
        step = int(input("Ход игрока № 2: "))

    napole(step, symbol)  # делаем ход в указанную ячейку
    win = get_result()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
pole_vidim()
print("Победил игрок играющий ", win)