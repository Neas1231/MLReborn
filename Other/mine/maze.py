from collections import Counter
import datetime


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


def set_new_dynamite(coors, field):
    if field[coors[0]][coors[1]] != '.':
        return False
    field[coors[0]][coors[1]] = '='
    return True


def generation_new_chest_field(field):
    from random import randint
    while True:
        if set_new_chest((randint(0, len(field) - 1), randint(0, len(field[0]) - 1)), field):
            break


def generation_new_dynamite_field(field):
    from random import randint
    while True:
        if set_new_dynamite((randint(0, len(field) - 1), randint(0, len(field[0]) - 1)), field):
            break


def generation_field(quantity_field_x=20, quantity_field_y=20, quantity_chest=2, quantity_stone=33,
                     quantity_dynamite=1):
    from random import randint
    result_field = []
    for i in range(quantity_field_x):
        result_field.append([])
        for __ in range(quantity_field_y):
            result_field[i].append('.')

    result_field[2][2] = '&'

    while quantity_chest > 0:
        if set_new_chest((randint(0, quantity_field_x - 1), randint(0, quantity_field_x - 1)), result_field):
            quantity_chest -= 1

    while quantity_stone > 0:
        if set_new_stone((randint(0, quantity_field_x - 1), randint(0, quantity_field_x - 1)), result_field):
            quantity_stone -= 1

    while quantity_dynamite > 0:
        if set_new_dynamite((randint(0, quantity_field_x - 1), randint(0, quantity_field_x - 1)), result_field):
            quantity_dynamite -= 1

    flatten_generated_field = [item for subl in result_field for item in subl]
    return result_field, Counter(flatten_generated_field)


def show_field(data_user):
    print(f'======= SCORE: {data_user["score"]} ====== Dynamite: {data_user["dynamite"]}')
    for row in data_user['field']:
        print('|', *row, '|')


def is_check_inside_border(check_position, field, dynamite_count):
    if not (check_position[0] >= 0 and check_position[1] >= 0 \
            and check_position[0] < len(field) and check_position[1] < len(field[0])):
        return False
    if field[check_position[0]][check_position[1]] == '#' and dynamite_count > 0:
        command_user = input("Использовать динамит?\n'y'-да\n'n'-нет")
        match command_user.lower():
            case 'y':
                return True
            case 'n':
                return False
    if field[check_position[0]][check_position[1]] == '#':
        return False
    return True


def set_new_position(new_coors, coors_before, data_user, true_data_field):
    if data_user['field'][new_coors[0]][new_coors[1]] == '%':
        data_user['score'] += 1
        generation_new_chest_field(data_user['field'])
    if data_user['field'][new_coors[0]][new_coors[1]] == '=':
        data_user['dynamite'] += 1
        generation_new_dynamite_field(data_user['field'])
    if data_user['field'][new_coors[0]][new_coors[1]] == '#':
        data_user['dynamite'] -= 1
        true_data_field['#'] -= 1
        true_data_field['.'] += 1

    data_user['field'][new_coors[0]][new_coors[1]] = '&'
    data_user['field'][coors_before[0]][coors_before[1]] = '.'
    return data_user


def game(field, true_data_field):
    data_user = {'field': field, 'score': 0, 'dynamite': 0}
    point_game = (2, 2)
    command_user = ''
    step = 0
    while command_user.lower() != 'q':
        new_coors = False
        show_field(data_user)
        command_user = input('"a"-влево\n"s"-вниз\n"d"-вправо\n"w"-вверх\nваш ход:')
        match command_user.lower():
            case 'a':
                new_coors = (point_game[0], point_game[1] - 1)
            case 'd':
                new_coors = (point_game[0], point_game[1] + 1)
            case 's':
                new_coors = (point_game[0] + 1, point_game[1])
            case 'w':
                new_coors = (point_game[0] - 1, point_game[1])
        if new_coors:
            if is_check_inside_border(new_coors, data_user['field'], data_user['dynamite']):
                data_user = set_new_position(new_coors, point_game, data_user, true_data_field)
                point_game = new_coors
            else:
                print('туда нельзя двигаться, там стена')
        step += 1
        if step % 3 == 0:
            flatten_user_field = [item for subl in data_user['field'] for item in subl]
            data_current_field = Counter(flatten_user_field)
            with open('./log.txt', 'a') as f:
                if data_current_field == true_data_field:
                    print('ok')
                    f.write(f'{datetime.datetime.now()} - OK\n')
                else:
                    print('ne ok')
                    difference = {x: data_current_field[x] - true_data_field[x] for x in data_current_field if
                                  x in true_data_field}
                    f.write(f'{datetime.datetime.now()} - не хватает: {difference}\n')


game(*generation_field())
