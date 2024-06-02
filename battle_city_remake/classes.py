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
class Block(sprite.Sprite, Reset):
    def __init__(self, image_file, sprite_size, x, y, hp = 10):
        super().__init__()
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 10

#класс Unit
class Unit(sprite.Sprite, Reset):
    def __init__(self, image_file, sprite_size, x, y, direction, speed = 2, damage = 5):
        super().__init__()
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
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

    def movement(self, group):
        left_side = Rect(self.rect.left - 1, self.rect.top, 1, self.rect.height)
        right_side = Rect(self.rect.right, self.rect.top, 1, self.rect.height)
        top_side = Rect(self.rect.left, self.rect.top - 1, self.rect.width, 1)
        bottom_side = Rect(self.rect.left, self.rect.bottom, self.rect.width, 1)

        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and not left_side.colliderect(group):
            self.direction = LEFT
            self.rect.x -= self.speed
        elif keys_pressed[K_d] and not right_side.colliderect(group):
            self.direction = RIGHT
            self.rect.x += self.speed
        elif keys_pressed[K_w] and not top_side.colliderect(group):
            self.direction = UP
            self.rect.y -= self.speed
        elif keys_pressed[K_s] and not bottom_side.colliderect(group):
            self.direction = DOWN
            self.rect.y += self.speed

    def fire(self):
        global timer_for_fire
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE] and timer_for_fire >= 30:
            if self.direction == RIGHT:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, RIGHT))
            elif self.direction == LEFT:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, LEFT))
            elif self.direction == DOWN:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, DOWN))
            elif self.direction == UP:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, UP))
            timer_for_fire = 0
        timer_for_fire += 1

#класс Enemy
class Enemy(Unit, Destroy):
    def movement(self):
        pass

player = Player(texture_player1, (50, 50), 100, 100, RIGHT)

block1 = Block(texture_block, (50, 50), 200, 200)