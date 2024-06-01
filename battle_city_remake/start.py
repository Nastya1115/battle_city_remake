# этот модуль нужен для импорта остальных модулей, а также базовых настроек и переменных

from pygame import *
from textures import *

clock = time.Clock()

#переменные
game_run = True
bullets = list()

#настройки
WIN_SIZE = (500, 500)
FPS = 120

#константы
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'

#окно
window = display.set_mode(WIN_SIZE)
display.set_caption("battle city remake") 