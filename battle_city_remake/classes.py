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

#класс Block
class Block(sprite.Sprite):
    def __init__(self, image_file, sprite_size, x, y, hp = 10):
        super().__init__()
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#класс Unit
class Unit(sprite.Sprite, Reset):
    def __init__(self, image_file, sprite_size, x, y, direction, speed = 5, damage = 5):
        super().__init__()
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.damage = 5
        self.direction = direction

#класс Bullet
class Bullet(Unit):

    def movement(self):
        if self.direction == LEFT:
                self.rect.x -= self.speed
        elif self.direction == RIGHT:
                self.rect.x += self.speed
        elif self.direction == UP:
                self.rect.y -= self.speed
        elif self.direction == DOWN:
                self.rect.y += self.speed

#класс Player
class Player(Unit):

    def movement(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a]:
            self.direction = LEFT
            self.rect.x -= self.speed
        elif keys_pressed[K_d]:
            self.direction = RIGHT
            self.rect.x += self.speed
        elif keys_pressed[K_w]:
            self.direction = UP
            self.rect.y -= self.speed
        elif keys_pressed[K_s]:
            self.direction = DOWN
            self.rect.y += self.speed

    def fire(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE]:
            if self.direction == RIGHT:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, RIGHT))
            elif self.direction == LEFT:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, LEFT))
            elif self.direction == DOWN:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, DOWN))
            elif self.direction == UP:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, UP))

#класс Enemy
class Enemy(Unit, Destroy):
    def movement(self):
        pass

player = Player(texture_player, (50, 50), 100, 100, RIGHT)

block = Block(texture_block, (50, 50), 100, 100)