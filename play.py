def greet():
    print("_________________")
    print("Приветсвуеm вас")
    print("    в игре     ")
    print("крестики-нолики")
    print("_________________")
    print("формат ввода: x y")
    print("x - номер строки ")
    print("y - номерстолбца ")

greet()

from dataclasses import field

field = [[" "] * 3 for i in range(3) ]
#field [0][1] = "X"
#field [0][2] = "X"
#field [0][0] = "0"
def show():
    print(f" 0 1 2")
    for i in range(3):
        row_info = " " . join(field[i])
        #print(f"{i} {field[i][0]} {field[i][1]} {field[i][2]}")
        print(f"{i} {row_info}")
def show():
    print()
    print("   | 0 | 1 | 2 | ")
    print(" _______________ ")
    for i, row in enumerate(field):
        row_str = f" {i} | {' | ' . join(row)} | "
        print(row_str)
        print(" _______________ ")
    print()

show()

def ask():
    x, y = map(int, input("   ваш ход ").split())
    while x < 0 or x > 2 or y < 0 or y > 2:
        x, y = map(int, input("   ваш ход ").split())
    return  x, y
def ask():
    while True:
        x, y = map(int, input("   ваш ход ").split())
        if 0 <= x <= 2 and 0 <= y <= 2 :
#            if field[x][y] == " ":
#            return x, y
#            else:
 #               print(" клетка занята! ")
#        else:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != " ":
            print(" клетка занята! ")
            continue
        return x, y
def ask(cords=None):
    while True:
        cords = input(" ваш ход ").split()
        if len(cords) != 2:
            print(" Введите 2 кординаты! ")
            continue
        x, y = cords
        if not(x.isdigit()) or not(y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y > 2:
            print(" Координаты вне диапазона! ")
            continue
        if field[x][y] != " ":
            print(" клетка занята!")
            continue
        return x, y

ask()

def check_win(win_cord=None, symbols=None):
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[i][j])
        if symbols == ["x","x","x"]:
            return True

    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(field[j][i])
        if symbols == ["x", "x", "x"]:
            return True

        symbols = []
        for i in range(3):
            symbols.append(field[i][i])
        if symbols == ["x", "x", "x"]:
            return True


        symbols = []
        for i in range(3):
            symbols.append(field[i][2-i])
        if symbols == ["x", "x", "x"]:
            return True
#    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
#                ((2, 0), (2, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
#                ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
#                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
#    for cord in win_cord:
#        symbols = []
#
#        for c in cord:
#            symbols.append(field[c[0][c[1]]])
#        if symbols == ["x", "x", "x"]:
#            print("Выиграл x!!!")
#            return True
#        if symbols == ["o", "o", "o"]:
#            print("Выиграл o!!!")
#            return True
        return False

#        a = cord[0]
#        b = cord[1]
#        c = cord[2]
#        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != " ":
#            print(f"Выиграл {field[a[0]][a[1]]}! ")
#            return True
#        return False
check_win()

num = 0
while True:
    show()
    num += 1
    if num % 2 == 1:
        print(" Ходит крестик ")
    else:
        print(" Ходит нолик ")
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = 'x'
    else:
        field[x][y] = "o"

    if check_win():
        print("Ввыгроли")
        break
    if num == 9:
            print("Ничья")
            break
