# этот модуль нужен для классов

from start import *

#
#       ВСПОМАГАТЕЛЬНЫЕ КЛАССЫ
#

#класс Reset
class Reset():
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс Change_image
class Change_image():
    def change_image(self, image_file):
        logging.info('Image changed')
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        
#класс Animation
class Animation(Change_image):
    def animation(self, list):
            if self.index < len(list) - 1:
                self.index += 1
                self.change_image(list[self.index])
            else:
                self.index = 0

#
#       ОСНОВНЫЕ КЛАССЫ
#

#класс Counter
class Counter(sprite.Sprite):
    def __init__(self):
        self.killed = 0

    def reset(self, player):
        self.enemies_killed = font.render(f"Убито врагов: {self.killed}", True, (255,255,255))
        self.player_hp = font.render(f"Здоровье: {player.hp}", True, (255,255,255))

        window.blit(self.enemies_killed, (WIN_SIZE[0] - 200, 0))
        window.blit(self.player_hp, (WIN_SIZE[0] - 200, 30))

#класс Explosion
class Explosion(sprite.Sprite, Change_image, Reset):
    def __init__(self, x, y, image_file = explosion1, index = 0, sprite_size = SPRITE_SIZE):
        super().__init__()
        self.sprite_size = SPRITE_SIZE
        self.image = transform.scale(image.load(explosion1), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.index = 0

    def animation(self):
        if self.index < len(explosions) - 1:
            self.index += 1
            self.change_image(explosions[self.index])
        else:
            effects.remove(self)

#класс GameObject
class GameObject(sprite.Sprite, Reset):
    def __init__(self, image_file, sprite_size, x, y):
        super().__init__()
        logging.info('Unit created')
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#класс ImageButton
class ImageButton():
    def __init__(self, x, y, width, height, text, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

#класс Block
class Block(GameObject):
    def __init__(self, x, y, image_file, sprite_size, hp = 10):
        super().__init__(image_file, sprite_size, x, y)
        self.hp = hp

#
#       КЛАССЫ ДВИГАЮЩИХСЯ ОБЬЕКТОВ
#

#класс Unit
class Unit(GameObject):
    def __init__(self, x, y, image_file, sprite_size, direction, speed = 2, damage = 5, hp = 15, index = 0):
        super().__init__(image_file, sprite_size, x, y)
        self.speed = speed
        self.damage = damage
        self.hp = hp
        self.direction = direction
        self.index = 0

#класс Bullet
class Bullet(Unit):
    def __init__(self, x, y, image_file, sprite_size, direction, bullet_type, speed = 2, damage = 5, hp = 1):
        super().__init__(x, y, image_file, sprite_size, direction, speed, damage, hp)
        self.bullet_type = bullet_type

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
class Player(Unit, Animation):
    def movement(self, group):
        # обозначение сторон хитбокса
        self.left_side = Rect(self.rect.left - 1, self.rect.top, 1, self.rect.height)
        self.right_side = Rect(self.rect.right, self.rect.top, 1, self.rect.height)
        self.top_side = Rect(self.rect.left, self.rect.top - 1, self.rect.width, 1)
        self.bottom_side = Rect(self.rect.left, self.rect.bottom, self.rect.width, 1)

        # нажатие на кнопки и движение
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and not self.left_side.collidelistall(group):
            self.animation(player_left)
            self.direction = LEFT
            self.rect.x -= self.speed
        elif keys_pressed[K_d] and not self.right_side.collidelistall(group):
            self.animation(player_right)
            self.direction = RIGHT
            self.rect.x += self.speed
        elif keys_pressed[K_w] and not self.top_side.collidelistall(group):
            self.animation(player_up)
            self.direction = UP
            self.rect.y -= self.speed
        elif keys_pressed[K_s] and not self.bottom_side.collidelistall(group):
            self.animation(player_down)
            self.direction = DOWN
            self.rect.y += self.speed

    def fire(self):
        global timer_for_fire
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE] and timer_for_fire >= 60:
            if self.direction == LEFT:
                bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet_right, (50, 50), LEFT, FRIENDLY))
            elif self.direction == RIGHT:
                bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet_left, (50, 50), RIGHT, FRIENDLY))
            elif self.direction == DOWN:
                bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet_down, (50, 50), DOWN, FRIENDLY))
            elif self.direction == UP:
                bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet, (50, 50), UP, FRIENDLY))
            timer_for_fire = 0
        timer_for_fire += 1
             
#класс Basic_Enemy
class Basic_Enemy(Unit, Animation):
    def move(self, group, images_up, images_down, images_left, images_right):
        self.left_side = Rect(self.rect.left - 1, self.rect.top, 1, self.rect.height)
        self.right_side = Rect(self.rect.right, self.rect.top, 1, self.rect.height)
        self.top_side = Rect(self.rect.left, self.rect.top - 1, self.rect.width, 1)
        self.bottom_side = Rect(self.rect.left, self.rect.bottom, self.rect.width, 1)

        if self.direction == LEFT and not self.left_side.collidelistall(group):
            self.rect.x -= self.speed
            self.animation(images_left)
        elif self.direction == RIGHT and not self.right_side.collidelistall(group):
            self.rect.x += self.speed
            self.animation(images_right)
        elif self.direction == UP and not self.top_side.collidelistall(group):
            self.rect.y -= self.speed
            self.animation(images_up)
        elif self.direction == DOWN and not self.bottom_side.collidelistall(group):
            self.rect.y += self.speed
            self.animation(images_down)

    def fire(self):
        if self.direction == LEFT:
            bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet_right, (50, 50), LEFT, NOT_FRIENDLY))
        elif self.direction == RIGHT:
            bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet_left, (50, 50), RIGHT, NOT_FRIENDLY))
        elif self.direction == DOWN:
            bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet_down, (50, 50), DOWN, NOT_FRIENDLY))
        elif self.direction == UP:
            bullets.append(Bullet(self.rect.x, self.rect.y, texture_bullet, (50, 50), UP, NOT_FRIENDLY))

#
#       КЛАССЫ ВРАГОВ
#

# Абстрактный класс врага
class Enemy(ABC, Basic_Enemy):
    def __init__(self, image_file, sprite_size, x, y, direction, timer = 0, speed = 2, damage = 5, hp = 15):
        super().__init__(image_file, sprite_size, x, y, direction, speed, damage, hp)
        self.timer = 0
    
    @abstractmethod
    def movement(self):
        pass

# класс врага(1 уровень)
class EnemySilver(Enemy):

    def movement(self, group):  

        self.move(group, silver_tank_up, silver_tank_down, silver_tank_left, silver_tank_right)

        if self.timer == 60:
            self.direction = choice((LEFT, RIGHT))
            self.timer = 0
            self.fire()
        self.timer += 1
        
# класс врага(2 уровень)       
class EnemyGold(Enemy):

    def movement(self, group):  

        self.move(group, gold_tank_up, gold_tank_down, gold_tank_left, gold_tank_right)

        if self.timer == 60:
            self.direction = choice((LEFT, RIGHT, UP, DOWN))
            self.timer = 0
            self.fire()
        self.timer += 1
        
# класс врага(3 уровень)      
class EnemyDiamond(Enemy):

    def movement(self, group):  

        self.move(group, gold_tank_left, gold_tank_down, gold_tank_left, gold_tank_right)

        if self.timer == 60:
            self.direction = choice((LEFT, RIGHT, UP, DOWN))
            self.timer = 0
            self.fire()
        self.timer += 1

#
#       ФАБРИКИ
#

# Абстрактная фабрика для создания врагов
class EnemyFactory(ABC):
    @abstractmethod
    def create_enemy(self, image_file, sprite_size, x, y, direction):
        pass

# Конкретная фабрика для создания врагов первого уровня
class SilverEnemyFactory(EnemyFactory):
    def create_enemy(self, image_file, sprite_size, x, y, direction):
        return EnemySilver(image_file, sprite_size, x, y, direction)

# Конкретная фабрика для создания врагов второго уровня
class GoldEnemyFactory(EnemyFactory):
    def create_enemy(self, image_file, sprite_size, x, y, direction):
        return EnemyGold(image_file, sprite_size, x, y, direction)

# Конкретная фабрика для создания врагов третьего уровня
class DiamondEnemyFactory(EnemyFactory):
    def create_enemy(self, image_file, sprite_size, x, y, direction):
        return EnemyDiamond(image_file, sprite_size, x, y, direction)
    

#сами фабрики
silver_factory = SilverEnemyFactory()
gold_factory = GoldEnemyFactory()
diamond_factory = DiamondEnemyFactory()