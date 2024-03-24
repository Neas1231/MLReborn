
def set_new_chest(coors, field):
    if field[coors[0]][coors[1]] != '.':
        return False
    field[coors[0]][coors[1]] = '%'
    return True

def set_new_stone(coors, field):
    if field[coors[0]][coors[1]] != '.':
        return False
    field[coors[0]][coors[1]] = '#'
    return True


def generation_new_chest_field(field):
    from random import randint
    while True:
        if set_new_chest((randint(0, len(field)-1), randint(0, len(field[0])-1)), field):
            break


def generation_field(quantity_field_x=20, quantity_field_y=20, quantity_chest=2, quantity_stone=33):
    from random import randint
    result_field = []
    for i in range(quantity_field_x):
        result_field.append([])
        for __ in range(quantity_field_y):
            result_field[i].append('.')

    result_field[2][2] = '&'

    while quantity_chest > 0:
        if set_new_chest((randint(0, quantity_field_x-1), randint(0, quantity_field_x-1)), result_field):
            quantity_chest -= 1
    
    while quantity_stone > 0:
        if set_new_stone((randint(0, quantity_field_x-1), randint(0, quantity_field_x-1)), result_field):
            quantity_stone -= 1
        
    return result_field

def show_field(data_user):
    print(f'======= SCORE: {data_user["score"]} ======')
    for row in data_user['field']:
        print('|',*row, '|')


def is_check_inside_border(check_position, field):
    if check_position[0] >= 0 and check_position[1] >= 0 \
        and check_position[0] < len(field) and check_position[1] < len(field[0]) and field[check_position[0]][check_position[1]] != '#':
        return True
    return False

def set_new_position(new_coors, coors_before, data_user):
    if data_user['field'][new_coors[0]][new_coors[1]] == '%':
        data_user['score'] += 1
        generation_new_chest_field(data_user['field'])
    data_user['field'][new_coors[0]][new_coors[1]] = '&'
    data_user['field'][coors_before[0]][coors_before[1]] = '.'
    return data_user


def game(field):
    data_user = {'field':field, 'score':0}
    point_game = (2,2)
    command_user = ''
    while command_user.lower() != 'q':
        new_coors = False
        show_field(data_user)
        command_user = input('"a"-влево\n"s"-вниз\n"d"-вправо\n"w"-вверх\nваш ход:')
        match command_user.lower():
            case 'a':
                new_coors = (point_game[0], point_game[1]-1)
            case 'd':
                new_coors = (point_game[0] ,point_game[1]+1)
            case 's':
                new_coors = (point_game[0]+1, point_game[1])
            case 'w':
                new_coors = (point_game[0]-1, point_game[1])
        if new_coors:
            if is_check_inside_border(new_coors, data_user['field']):
                data_user = set_new_position(new_coors, point_game, data_user)
                point_game = new_coors
            else:
                print('туда нельзя двигаться, там стена')
            
            

game(generation_field())



# ЛАБА
# Необходимо написать функцию для проверки корректности отображения всех элементов
# через каждый третий ход, проверяет все ли элементы на поле - игрок, стены и сундуки.
# логировать результаты.
# записать в файл дату проверки и результат.
# Результат в формате:
# дата - OK
# дата - написать чего не хватает и сколько
        


# ЛАБА.
# добавить вариант сбора выпадания динамита. Который можно собрать. Затем, если стоишь возле стены, есть возможность применить динамит. который может разрушить стену

# *
# добавить кнопки управления.

