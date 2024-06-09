# 0 - empty
# p - player
# b - block

from classes import *

#карта 1
level_1 = [
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', '0', '0', '0', '0', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', '0', 'e', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', 'b', 'b', 'b', 'b', '0', '0', 'b'],
    ['b', '0', '0', '0', 'b', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', '0', 'b', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', '0', 'b', 'b', 'b', '0', '0', 'b'],
    ['b', '0', 'p', '0', '0', '0', '0', '0', 'e', 'b'],
    ['b', '0', '0', '0', '0', '0', '0', '0', '0', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
]

#настройки
player = None

blocks = []
enemies = []

pixel = 50

#генерация карты
def Map_generation(level):
    #перебор массива
    for y, row in enumerate(level):
        y *= pixel
        for x, type in enumerate(row):
            x *= pixel

            #игрок
            if type == 'p':
                global player
                player = Player(texture_player1, SPRITE_SIZE, x, y, RIGHT)

            #враг
            elif type == 'e':
                enemies.append(choice(((silver_factory.create_enemy(silver_tank, SPRITE_SIZE, x, y, RIGHT)), (gold_factory.create_enemy(gold_tank, SPRITE_SIZE, x, y, RIGHT)))))

            #блок
            elif type == 'b':
                blocks.append(Block(texture_block, SPRITE_SIZE, x, y))

Map_generation(level_1)
