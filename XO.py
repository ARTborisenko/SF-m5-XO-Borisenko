def prt_m(): #Печать матрицы
    for i in matrix:
        print(*i)

def inp(L): #Проверка вводимых данных
    if L != [] and len(L) != 1:
        for i in L:
            if (1 != i and 2 != i and 3 != i):
                print('Некорректный ввод!!!')
                return False
        return True
    else:
        print('Некорректный ввод!!!')
        return False

def winner(list): #Проверка на победителя
    for i in win_list:
        if all(x in list for x in i):
            return True
    return False

def go_x(): #Ход игрока Х с проверкой, не занята ли ячейка
    while True:
        move_x = list(map(int, input('Ходит X, введите координату через пробел: ').split()))
        if inp(move_x):
            if move_x in moves:
                print('Ячейка занята!!!')
                continue
            else:
                moves.append(move_x)
                moves_x.append(move_x)
                matrix[moves[-1][0]][moves[-1][1]] = 'X'
                prt_m()
                if winner(moves_x):
                    print("Победа игрока X!!!")
                break

def go_y(): #Ход игрока У с проверкой, не занята ли ячейка
    while True:
        move_y = list(map(int, input('Ходит Y, введите координату через пробел: ').split()))
        if inp(move_y):
            if move_y in moves:
                print('Ячейка занята!!!')
                continue
            else:
                moves.append(move_y)
                moves_y.append(move_y)
                matrix[moves[-1][0]][moves[-1][1]] = 'Y'
                prt_m()
                if winner(moves_y):
                    print("Победа игрока Y!!!")
                break

#Все возможные комбинации победы:
win_list = [
    [[1, 1],[1, 2],[1, 3]],
    [[2, 1],[2, 2],[2, 3]],
    [[3, 1],[3, 2],[3, 3]],
    [[1, 1],[2, 1],[3, 1]],
    [[1, 2],[2, 2],[3, 2]],
    [[1, 3],[2, 3],[3, 3]],
    [[1, 1],[2, 2],[3, 3]],
    [[1, 3],[2, 2],[3, 1]],
    ]

#Матрица, она же игровое поле
matrix = [
    [' ', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-'],
    ]

#Списки где хранятся все ходы и ходы игроков по отдельности
moves = []
moves_x = []
moves_y = []

#Печатаем матрицу перед стартом хода
prt_m()

#Запускаем код
while True:
    if not winner(moves_y):
        go_x()
    else:
        break
    if len(moves) == 9:
        print("Ничья!")
        break
    if not winner(moves_x):
        go_y()
    else:
        break