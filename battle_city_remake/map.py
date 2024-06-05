# 0 - empty
# p - player
# b - block

from classes import *

level_1 = [
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', '0', '0', '0', '0', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', '0', '0', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', 'b', 'b', 'b', 'b', '0', '0', 'b'],
    ['b', '0', '0', '0', 'b', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', '0', 'b', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', '0', 'b', 'b', 'b', '0', '0', 'b'],
    ['b', '0', 'p', '0', '0', '0', '0', '0', '0', 'b'],
    ['b', '0', '0', '0', '0', '0', '0', '0', '0', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
]

player = None

blocks = []

pixel = 50

def Map_generation(level):
    for y, row in enumerate(level):
        y *= pixel
        for x, type in enumerate(row):
            x *= pixel

            if type == 'p':
                global player
                player = Player(texture_player1, SPRITE_SIZE, x, y, RIGHT)

            elif type == 'b':
                blocks.append(Block(texture_block, SPRITE_SIZE, x, y))

Map_generation(level_1)
