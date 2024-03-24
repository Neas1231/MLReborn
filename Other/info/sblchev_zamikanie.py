# test = '111'
# print(id(test))

# test2 = test
# print(id(test2))
# test2 += '2'
# print(id(test2))

# test = [1,2,3]
# print(id(test))
# test2 = test
# print(id(test2))
# test2.append(4)
# print(id(test2))

# test = {
#     1:[1,2,3,4], 
#     2:[2,3,4,5],
#     3:[2,3,4,5],
#     4:[2,3,4,5],
#     }

# tother = {**{'2': [2, 3, 4, 5]}}

# print(tother)

# test = [
#     {'запрос1': 'какая планета самая большая в нашей солнечной системе'}, 
#     {'запрос2': 'какая масса этой планеты'}
# ]

# [
#     {'запрос1': 'какая планета самая большая в нашей солнечной системе'}, 
#     {'запрос2': 'какая масса этой планеты'}, 
#     {'now_response': 'какой размер этой планеты'}]

# [
#  {'запрос1': 'какая планета самая большая в нашей солнечной системе'}, 
#  {'запрос2': 'какая масса этой планеты'}, 
#  {'now_res': 'текущий запрос в GPT'}
#  ]

# def response_(respons):
#     return respons

# def response_gpt(context, now_res):
#     return response_(
#         [
#             *context,
#             {'now_res':now_res}
#         ]
#     )

# print(response_gpt(test, 'какой размер этой планеты'))


# ```python
# {**{'2': [2, 3, 4, 5]}}
# ```

# В этом случае, словарь будет распакован, и вы получите его содержимое.`

# def test(num):
#     return num * 10


# z = test
# print(type(z))
# # if z == test:
# #     print('Да действительно ни равны')
# # test2 = z
# # xx = test2(1000)
# print(xx)

# def test(num, arr=[]):
#     arr=[]
#     arr.append(num)
#     return arr

# print(test(1))
# print(test(2))
# print(test(3))
test = []

def test(name):

    def inner(health):
        def inner2(new_name=''):
            if new_name:
                nonlocal name
                name = new_name
        # print(f'Привет {name} количество жизни: {health}')
            return f'Привет {name} количество жизни: {health}'
        return inner2
    # функция inner НЕ ВЫЗЫВАЕТСЯ
    return inner
    
# devid = test('Девид')
# nadejda = test('Надежда')
# aleksandr = test('Александр')

# devid = devid(200)
# nadejda = nadejda(150)
# aleksandr = aleksandr(90)

# print(devid())
# print(nadejda())
# print(aleksandr())

# print(devid('Сергей'))
# print(nadejda('Наталья'))
# print(aleksandr('Вася'))
# print('окончание работы программы')

# import random



# from random import *

# from random import randint

# print(randint(1,10))

def test(name):

    def inner(health):
        # может совершать какие-то манипуляции с аргументами
        def inner2(new_name=''):
            if new_name:
                nonlocal name
                name = new_name
        # print(f'Привет {name} количество жизни: {health}')
            return f'Привет {name} количество жизни: {health}'
        return inner2()
    # функция inner НЕ ВЫЗЫВАЕТСЯ
    return inner


# сгененировать переменные с монстрами
# у которого есть имя, жизни, защита, атака
# а при вызове внутренней функции, он выдает список сгенерированного монстра (имя, жизни, защита, атака)



# from random import randint

# def first(name):
#     # вот здесь!
#     def second():
#         hp = randint(1, 100)
#         armor = randint(1, 100)
#         damage = randint(1, 100)
#         return name, hp, armor, damage
#     return second

# test = first('Александр')
# print(test())

list_pers = ['люди', 'орк', 'эльф']

from random import randint

def pers(pers):
    def gerenerate():
        if pers == 'люди':
            health = randint(100, 200)
            attack = randint(50, 150)
        elif pers == 'орк':
            health = randint(200, 400)
            attack = randint(100, 250)
        elif pers == 'эльф':
            health = randint(50, 100)
            attack = randint(30, 110)
        def results():
            return pers, health, attack
        return results
    return gerenerate

# player1 = pers('орк')
# player1 = player1()
# print(player1)
# player2 = pers('эльф')
# player2 = player2()
# print('вывод')
# resl1 = player1()
# print(resl1)
# resl2 = player2()
# print(resl2)




from random import randint, choice

# def generate_name():
#     word_1 = ['Тролль', 'Огр', 'Краб', 'Элементаль', 'Гоблин', 'Орк', 'Дракон', 'Бес', 'Гарпия', 'Бандит', 'Зомби', 'Лич', 'Вампир', 'Грифон']
#     word_2 = ['Призрачный', 'Огненный', 'Жуткий', 'Каменный', 'Летучий', 'Лютый', 'Хитрый', 'Могучий', 'Страшный', 'Мертвый', 'Беспощадный', 'Колючий', 'Ядовитый', 'Кристальный']
    
#     return f'{choice(word_2)} {choice(word_1)}'


# def generate_monsters():
#     word_1 = ['Тролль', 'Огр', 'Краб', 'Элементаль', 'Гоблин', 'Орк', 'Дракон', 'Бес', 'Гарпия', 'Бандит', 'Зомби', 'Лич', 'Вампир', 'Грифон']
#     word_2 = ['Призрачный', 'Огненный', 'Жуткий', 'Каменный', 'Летучий', 'Лютый', 'Хитрый', 'Могучий', 'Страшный', 'Мертвый', 'Беспощадный', 'Колючий', 'Ядовитый', 'Кристальный']

#     monster = {'name': choice(word_2)+choice(word_1),
#               'hp': randint(30, 100),
#               'armor': randint(15, 60),
#               'damage': randint(10, 50),
#               }
    
#     def spawn():

#         print(f"Вызванный монстр {monster['name']} призван!")

#     return spawn
        

# monster1 = generate_monsters()
# print(monster1)
# monster1()

# monster2 = generate_monsters()
# monster2()

# monster2 = generate_monsters()
# monster2()



from random import choice, randint 
from string import ascii_lowercase
 
monsters = []
 
def generate_qual():
    lenght = 5
 
    def generate_name(length):
        letters = ascii_lowercase
        name =  ''.join(choice(letters) for i in range(length))
        monster = {}
        monster['name'] = name
 
        def generate_healt():
            healt = randint(50, 160)
            monster['healt'] = healt
 
            def generate_prot():
                protection = randint(1, 50)
                monster['protection'] = protection
 
                def generate_attak():
                    attak = randint(1, 50)
                    monster['attak'] = attak
                    monsters.append(monster)
 
                return generate_attak
            return generate_prot
        return generate_healt
    return generate_name
 
# monster1 = generate_qual()
# monster1 = monster1(5)
# monster1 = monster1()
# monster1 = monster1()
# monster1 = monster1()
 
# print(monsters)
# print('------------')
 
# monster2 = generate_qual()
# monster2 = monster2(5)
# monster2 = monster2()
# monster2 = monster2()
# monster2 = monster2()
 
# print(monsters)
# print('------------')
 
# monster3 = generate_qual()
# monster3 = monster3(5)
# monster3 = monster3()
# monster3 = monster3()
# monster3 = monster3()
 
# print(monsters)

# from russian_names import RussianNames
# import random




# def generate_monster():
#     name = RussianNames().get_person()
#     lives = random.randint(20, 100)
#     defense = random.randint(10, 30)
#     attack = random.randint(5, 20)

#     def inner_func():
#         return name, lives, defense, attack

#     return inner_func

# def display_monster(monster):
#     name, lives, defense, attack = monster()
#     print(monster())




# monster_generator = generate_monster()
# display_monster(monster_generator)


# def zam(name, balance):
#     def inner(transaction='', quantity=0):
#         nonlocal balance
#         if transaction == '-':
#             balance -= quantity
#         elif transaction == '+':
#             balance += quantity
#         return name, balance
#     return inner
    
# anna = zam('Анна', 10000)
# print(anna())
# balance = anna('-', 1000)
# print(balance)

# nikita = zam('Никита', 1_000_000)('+', 300_000)
# # nikita('-', 900_000)
# print(nikita)


# напишите функцию, которая на входе получает текст
# нужно убрать из текста следующие символы ( !?№;()%.,: )
# пользователь вводит слово, а вам нужно выдать количество слов в тексте, которые начинаются на этот символ

# example

'abc adf dcg dcg dcgr'

# adf
# 2
# dcg
# 3

def slova_koroche(input_text, starting_letter):
  
    cleaned_text = input_text.replace('!', '').replace('?', '').replace('№', '').replace(';', '').replace('(', '').replace(')', '').replace('%', '').replace('.', '').replace(',', '').replace(':', '')
    
    words = cleaned_text.split()
    
    count = 0
    for word in words:
        if word[0].lower() == starting_letter.lower():
            count += 1
    
    return count
 
# input_text = input("Введите текст: ")
# input_word = input("Введите слово: ")
 
# result = slova_koroche(input_text, input_word[0])
# print("Количество слов, начинающихся на букву {}: {}".format(input_word[0], result))


# ( !?№;()%.,: )

def test(text): 
    result_dict = {}
    for elem in '!?№;()%.,:':
        text1 = text.replace(elem, '')
    text1 = text.split()

    all_word = set()
    for word in text1:
        all_word.add(word)
        if result_dict.get(word[0]):
            result_dict[word[0]] += 1
        else:
            result_dict[word[0]] = 1
    del text1
    def result_text(word, output = False):
        if output:
            return text
        if not(word in all_word):
            return 'такого слова не было в тексте'
        return result_dict[word[0]]
    return result_text

    

    # for word in text:
    #     if result_dict.get(word):
    #         result_dict[word] += 1
    #     else:
    #         result_dict[word] = 1
    # return result_dict
my_list_text = []
while True:
    
    print('------ID`шник введенных текстов-----')
    for i in range(len(my_list_text)):
        print(f'[{i}] ', my_list_text[i]('', True)[:6]+' ...')
    print('---------')

    interfaca = input(f'1 - ввести новый текст\n2- вывести текст из списка\n3-поиск слова\n-->')
    if interfaca == '1':
        text = input('введите текст для анализа: ')
        my_list_text.append(test(text))
    elif interfaca == '2':
        id_text = input('введите ID текста который хотите увидеть: ')
        print(my_list_text[int(id_text)]('', True))
    elif interfaca == '3':
        find_word = input('введите слово которое нужно найти: ')
        print(my_list_text[int(id_text)](find_word))

# test1 = test('как хорошо живется на свете винни пуху у него жена и дети, а сам лопух')
# test2 = test('Ключевым моментом для понимания работы генераторов является то, при вызове yield функция не прекращает свою работу, а “замораживается” до очередной итерации, запускаемой функцией next(). Если вы в своем генераторе, где-то используете ключевое слово return, то дойдя до этого места будет выброшено исключение StopIteration, а если после ключевого слова return поместить какую-либо информацию, то она будет добавлена к описанию StopIteration.')
# print(test2('места'))
    

    
    
        


# print(test('asf, asf, gfd, dgf dgh'))



