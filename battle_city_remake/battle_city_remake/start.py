# этот модуль нужен для импорта остальных модулей, а также базовых настроек и переменных
import logging
from pygame import *
from textures import *

font.init()

logging.basicConfig(filename='battle_city.log', level=logging.INFO)

clock = time.Clock()

#переменные
game_run = True
bullets = list()
timer_for_fire = 0

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