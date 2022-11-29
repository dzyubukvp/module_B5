print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
print("*" * 6, " Игровое поле совпадает с цифровой клавиатурой ", "*" * 6)
# Поле с цифрами от 1 до 9
pole = list(range(1,10))
# Рисуем поле 3х3 располагая цифры как на цифровой клавиатуре
def draw_pole(pole):
   print("-" * 13)
   for i in reversed(range(3)):
      print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|")
      print("-" * 13)
# Организовываем диалог с игроками в порядке очередности хода.
# #Проверяем корректность ввода данных.
# Исключаем повторение хода в занятую ячейку

def take_input(player_enters):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_enters+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(pole[player_answer-1]) not in "XO"):
            pole[player_answer-1] = player_enters
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

# Организуем условия выигрыша
def check_win(pole):
   win_line = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for tt in win_line:
       if pole[tt[0]] == pole[tt[1]] == pole[tt[2]]:
          return pole[tt[0]]
   return False

# Текущий ход игры с счетчиком ходов
def main(pole):
    counter = 0
    win = False
    while not win:
        draw_pole(pole)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(pole)
           if tmp:
              print(tmp, " <<<= выиграл! =>>>")
              win = True
              break
        if counter == 9:
            print("GAME OVER!!!")
            print("Ничья!")
            break
    draw_pole(pole)
main(pole)

input("Нажмите Enter для выхода!")

