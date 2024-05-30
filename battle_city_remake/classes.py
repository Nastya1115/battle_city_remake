# этот модуль нужен для классов

from start import *

#класс Reset
class Reset():
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс Destroy
#этот класс скорее всего не понадобиться
class Destroy():
    pass

#класс Change_image
class Change_image():
    def change_image(self, image_file):
        self.image = transform.scale(image.load(image_file), self.sprite_size)

#класс Unit
class Unit(sprite.Sprite, Reset):
    def __init__(self, image_file, sprite_size, x, y, speed = 5, damage = 5, direction = RIGHT):
        super().__init__()
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#класс Player
class Player(Unit):
    def movement(self):
        pass

    def fire(self):
        pass

#класс Enemy
class Enemy(Unit, Destroy):
    def movement(self):
        pass

player = Player(texture_player, (50, 50), 100, 100)