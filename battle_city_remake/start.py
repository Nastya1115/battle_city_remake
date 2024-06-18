# этот модуль нужен для импорта остальных модулей, а также базовых настроек и переменных
import logging
from pygame import *
from textures import *
from sounds import *
from random import choice, randint
from abc import ABC, abstractmethod
import unittest
import sys
from queue import PriorityQueue


#inits
mixer.init()
font.init()

clock = time.Clock()

#музыка
def music_play(music_file, volume):
    sound = mixer.Sound(music_file)
    sound.set_volume(volume)
    sound.play()

#логги
open('battle_city.log', 'w').close()
logging.basicConfig(filename='battle_city.log', level=logging.INFO)

#переменные
game_run = True
bullets = list()
timer_for_fire = 0
lvl_counter = 0

#
effects = []

#настройки
WIN_SIZE = (800, 600)
FPS = 120

#константы
PIXEL = 50
SPRITE_SIZE = (50, 50)
BULLET_SIZE = (25, 25)
ROWS, COLS = WIN_SIZE[0] / PIXEL, WIN_SIZE[1] / PIXEL
FRIENDLY = 'players'
NOT_FRIENDLY = 'enemys'
RIGHT = 'right'
LEFT = 'left'
DOWN = 'down'
UP = 'up'

#цвета
MAIN_SCREEN = (0, 0, 0)		
GAME_SCREEN = (0, 0, 0)			
SETTINGS_SCREEN = (128, 128, 128)

#окно
window = display.set_mode(WIN_SIZE)
display.set_caption("battle city remake")

# настройки шрифта
font = font.Font(None, 36)
text_font = font.render(" ", True, (255,255,255))
text_rect = text_font.get_rect(center=(400,50))
