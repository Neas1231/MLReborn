# from msvcrt import getch
# while True:
#     n = ord(getch())
#     print(n)
#     if n == 8:
#         break

import random
from msvcrt import getch

class OutOfBoxError(BaseException):
    ...

class VoidError(BaseException):
    ...

def generation(box_scale, num_rocks):
    box = [[0] * box_scale for i in range(box_scale)]
    coords_rocks = list(map(
        list, zip([random.randrange(0, 20) for _ in range(num_rocks)], [random.randrange(0, 20) for _ in range(num_rocks)])
    ))
    # Расстановка
    # Поле с камнями
    for coord in coords_rocks:
        box[coord[0]][coord[1]] = ' '
    # Кораблик
    while True:
        user_coord = [random.randrange(0, 20) for _ in range(2)]
        if user_coord not in coords_rocks:
            break
        else:
            continue
    box[user_coord[0]][user_coord[1]] = '\033[31m' + "X" + '\033[0m'
    return box, coords_rocks, user_coord, box_scale


box, coords_rocks, user_coord, box_scale = generation(box_scale=20, num_rocks=20)
print("Управление на стрелочки")
print("Выход на backspace")
while True:
    print()
    for row in box:
        print(' '.join(map(str, row)))

    n = ord(getch())
    match n:
        case 72:
            box[user_coord[0]][user_coord[1]] = 0
            user_coord[0] -= 1
        case 75:
            box[user_coord[0]][user_coord[1]] = 0
            user_coord[1] -= 1
        case 77:
            box[user_coord[0]][user_coord[1]] = 0
            user_coord[1] += 1
        case 80:
            box[user_coord[0]][user_coord[1]] = 0
            user_coord[0] += 1
    try:
        if not(0 <= user_coord[0] <= box_scale-1 and 0 <= user_coord[1] <= box_scale-1):
            raise OutOfBoxError
        if not(user_coord not in coords_rocks):
            raise VoidError
    except OutOfBoxError:
        print('Вы вышли за карту')
        break
    except VoidError:
        print('Вы наткнулись на камень')
        break

    box[user_coord[0]][user_coord[1]] = '\033[31m' + "X" + '\033[0m'

    # 72 вверх 75 влево 77 вправо 80 вниз 8 backspace
    if n == 8:
        break
