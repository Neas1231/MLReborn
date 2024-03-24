def create_matrix():
    import numpy as np

    matrix = np.ones((21, 21))
    matrix[1:-1, 1:-1] = 0
    return matrix


def step(answer, matrix, x, y):
    if answer == 0:
        print('Вы остались на месте')
    elif answer == 1:
        y += 1
    elif answer == 2:
        x += 1
    elif answer == 3:
        x -= 1
    elif answer == 4:
        y -= 1
    cheak(matrix, x, y)
    return x, y


def cheak(matrix, x, y):
    if checking_the_field(matrix[x][y]):
        pass
    else:
        raise 'Вы врезались, выбирете другое направление...'
    return x, y


def checking_the_field(field):
    print(field)
    if field == 0:
        return True
    else:
        return False


def create_stones(matrix):
    from random import randint
    for _ in range(10):
        x = randint(1, 20)
        y = randint(1, 20)
        matrix[x][y] = 1
    return matrix


def interface():
    x = 10
    y = 10
    matrix = create_matrix()
    matrix[x][y] = 1
    matrix = create_stones(matrix)
    while True:
        print(matrix)
        try:
            answer = int(input(
                'Выберите направление куда вы выдвинетесь\nНаверх - 1\nВправо - 2\nВлево - 3\nВниз - 4\nВыйти - 5 \n------> '))
            x, y = step(answer, matrix, x, y)
            matrix[x][y] = 1

            if answer == 5:
                break
                raise ValueError('Вы ввели некорректное число')

        except ValueError as err:
            print(err)
            break

interface()