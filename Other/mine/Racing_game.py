import random as rnd
import itertools


class Car:
    def __init__(self, health, max_speed, speed):
        self.max_health = health
        self.health = health
        self.max_speed = max_speed
        self.min_speed = 0
        self.speed = speed
        self.distance = 0
        self.before_turn = 0
        self.finishing = False

    def speedup(self, boost):
        max_boost = self.max_speed - self.speed
        if boost > max_boost:
            self.speed += max_boost
        else:
            self.speed += boost

    def slowdown(self, deceleration):
        max_slowdown = self.speed - self.min_speed
        if deceleration > max_slowdown:
            self.speed -= max_slowdown
        else:
            self.speed -= deceleration

    def get_damage(self):
        self.health -= (self.speed - 100) * 2
        self.max_speed -= round((self.max_health - self.health) * 1.225, 0)
        self.speed -= self.speed * 0.2
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def isdead(self):
        if self.health <= 0:
            print("Игрок взорвался")
            return True
        return False


class Default(Car):
    def __init__(self, name):
        super().__init__(100, 200, 70)
        self.name = name
        self.isability = True

    def ability(self):
        # _drift
        if self.speed > 100:
            self.speed = 100
        else:
            self.speed -= 20

    def ability_introduction(self):
        print('На скорости выше ста вы можете мгновенно затормозить до 100 пунктов')
        return ''


class Tank(Car):
    def __init__(self, name):
        super().__init__(120, 180, 70)
        self.name = name
        self.isability = True

    def ability(self):
        # _repair
        heal = 50
        max_heal = self.max_health - self.health
        if heal > max_heal:
            self.health += max_heal
        else:
            self.health += heal

    def ability_introduction(self):
        print('Чинит вашу машину на 50 пунктов')
        return ''


class Glass(Car):
    def __init__(self, name):
        super().__init__(80, 220, 70)
        self.name = name
        self.isability = True

    def ability(self):
        # _acceleration
        speedup = 40
        max_boost = self.max_speed - self.speed
        if speedup > max_boost:
            self.speed += max_boost
        else:
            self.speed += speedup

    def ability_introduction(self):
        print('Ускоряет вас на 40 пунктов за ход')
        return ''


class Race:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.random_scale = 1
        self.turning_player1 = False
        self.turning_player2 = False

    def introduction(self):
        print("\n___________________ВВЕДЕНИЕ______________________")
        return ('\
 Гонка 2000 пунктов, о поворотах предупреждается за 600 пунктов\n \
Каждая из машинок умеет ускоряться и замедляться на 20 пунктов, использовать способности\n \
Выигрывает тот кто преодолеет трассу, либо тот кто выживет\n \
Удачи всем игрокам')

    def player_move(self, player):
        print("\n")
        print(player.name)
        print("Статистика сейчас:")
        print(player.__class__.__name__)
        print(dict(itertools.islice(player.__dict__.items(), 7)), '\n')
        print("Выберите что вы будете делать:")
        print('Ускориться / Замедлиться / Использовать способность / Посмотреть статистику и способности')
        print('(1/2/3/4)')

        try:
            act = int(input())
            assert 1 <= act <= 4
        except:
            print('Вы ввели не правильно пропускаете ход')
            return False
        match act:
            case 1:
                try:
                    print("На сколько вы бы хотели ускориться? (5-20)")
                    boost = abs(int(input()))
                    assert 5 <= boost <= 20
                    player.speedup(boost)
                except:
                    boost = 5
                    player.speedup(boost)
            case 2:
                try:
                    print("На сколько вы бы хотели замедлиться? (5-20)")
                    slowdown = abs(int(input()))
                    assert 5 <= slowdown <= 20
                    player.slowdown(slowdown)
                except:
                    slowdown = 5
                    player.slowdown(slowdown)
            case 3:
                print("Ваша способность использована")
                if player.isability:
                    player.ability()
                    player.isability = False
                    print("Ваши параметры теперь:")
                    print(dict(itertools.islice(player.__dict__.items(), 7)), '\n')
                else:
                    print("Вы уже потратили способность!")
                    self.player_move(player)
            case 4:
                print("Ваша способность:")
                player.ability_introduction()
                self.player_move(player)

    def player_endmove(self, player):
        player.distance += player.speed
        player.before_turn -= player.speed
        if player.distance >= 2000:
            print(f'{player.name} - финишировал!!!!')
            player.finishing = True

    def is_turning(self):
        if ~self.turning_player1 and ~self.turning_player2:
            if rnd.randrange(100) < self.random_scale:
                self.random_scale = 1
                return True
            else:
                self.random_scale *= 1.5
                return False


if __name__ == "__main__":
    classes = [Default, Tank, Glass]
    print("Гоночки")
    print("Player 1, выбери себе машинку:")
    print('             hp  max_speed  speed')
    print(f'0: Default:  {Default("").health}     {Default("").max_speed}      {Default("").speed}', sep='\n')
    print(f'1: Tank:     {Tank("").health}     {Tank("").max_speed}      {Tank("").speed}', sep='\n')
    print(f'2: Glass:    {Glass("").health}      {Glass("").max_speed}      {Glass("").speed}', sep='\n')
    print('(0/1/2)')
    try:
        user_class = int(input())
        assert 0 <= user_class <= 2
        player1_class = classes[user_class]
    except:
        player1_class = classes[0]
    print("Player 2, выбери себе машинку:")
    print('             hp  max_speed  speed')
    print(f'0: Default:  {Default("").health}     {Default("").max_speed}      {Default("").speed}', sep='\n')
    print(f'1: Tank:     {Tank("").health}     {Tank("").max_speed}      {Tank("").speed}', sep='\n')
    print(f'2: Glass:    {Glass("").health}      {Glass("").max_speed}      {Glass("").speed}', sep='\n')
    print('(0/1/2)')
    try:
        user_class = int(input())
        assert 0 <= user_class <= 2
        player2_class = classes[user_class]
    except:
        player2_class = classes[0]
    print("Выберите имена игрокам:")
    player1_class = player1_class(input("Player 1 - "))
    player2_class = player2_class(input("Player 2 - "))
    print("\nВыбранные персонажи:")
    print(f"Player 1 - {type(player1_class).__name__}")
    print(f"Player 2 - {type(player2_class).__name__}")
    racing = Race(player1_class, player2_class)
    print(racing.introduction())
    while True:
        if racing.player1.finishing and ~(racing.player2.finishing):
            print(f"Победил {racing.player1.name}!!!")
            break
        if ~(racing.player1.finishing) and racing.player2.finishing:
            print(f"Победил {racing.player2.name}!!!")
            break

        if racing.player1.finishing and racing.player2.finishing:
            winner = [racing.player1.distance, racing.player2.distance].index(
                max([racing.player1.distance, racing.player2.distance]))
            match winner:
                case 0:
                    print(f"Победил {racing.player1.name}!!!")
                    break
                case 1:
                    print(f"Победил {racing.player2.name}!!!")
                    break

        if racing.turning_player1 and racing.player1.before_turn <= 0 and racing.player1.speed > 100:
            print("Player 1 не вошёл в поворот!!")
            racing.player1.get_damage()
            if racing.player1.isdead():
                print("Победитель Player 2!!!")
                break
            racing.turning_player1 = False

        if racing.turning_player2 and racing.player2.before_turn <= 0 and racing.player2.speed > 100:
            print("Player 2 не вошёл в поворот!!")
            racing.player2.get_damage()
            if racing.player2.isdead():
                print("Победитель Player 1!!!")
                break
            racing.turning_player2 = False

        racing.player_move(racing.player1)
        racing.player_endmove(racing.player1)
        racing.player_move(racing.player2)
        racing.player_endmove(racing.player2)
        if racing.is_turning():
            print("!!!!!!!!!!!!!!!!!!!!Поворооот!!!!!!!!!!!!!!!!!!!!")
            distances = [racing.player1.distance, racing.player2.distance]
            racing.turning_player1 = True
            racing.turning_player2 = True
            match distances.index(max(distances)):
                case 0:
                    racing.player1.before_turn = 600
                    racing.player2.before_turn = 600 + (racing.player1.distance - racing.player2.distance)
                    print(f"{racing.player1.name} до поворота:{racing.player1.before_turn}")
                    print(f"{racing.player2.name} до поворота:{racing.player2.before_turn}")
                case 1:
                    racing.player2.before_turn = 600
                    racing.player1.before_turn = 600 + (racing.player2.distance - racing.player1.distance)
                    print(f"{racing.player1.name} до поворота:{racing.player1.before_turn}")
                    print(f"{racing.player2.name} до поворота:{racing.player2.before_turn}")
