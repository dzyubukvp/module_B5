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

def napole(step,symbol):
    ind = pole.index(step)
    pole[ind] = symbol