# этот модуль нужен для классов

from start import *

#класс Reset
class Reset():
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс Change_image
class Change_image():
    def change_image(self, image_file):
        logging.info('Image changed')
        self.image = transform.scale(image.load(image_file), self.sprite_size)

#класс Enemy_movement
class Basic_Enemy():
    def move(self, group, images):
        #обозначение сторон хитбокса
        self.left_side = Rect(self.rect.left - 1, self.rect.top, 1, self.rect.height)
        self.right_side = Rect(self.rect.right, self.rect.top, 1, self.rect.height)
        self.top_side = Rect(self.rect.left, self.rect.top - 1, self.rect.width, 1)
        self.bottom_side = Rect(self.rect.left, self.rect.bottom, self.rect.width, 1)

        #движение
        if self.direction == LEFT  and not self.left_side.collidelistall(group):
            self.rect.x -= self.speed
            self.change_image(images[1])
        elif self.direction == RIGHT  and not self.right_side.collidelistall(group):
            self.rect.x += self.speed
            self.change_image(images[3])
        elif self.direction == UP  and not self.top_side.collidelistall(group):
            self.rect.y -= self.speed
            self.change_image(images[0])
        elif self.direction == DOWN  and not self.bottom_side.collidelistall(group):
            self.rect.y += self.speed
            self.change_image(images[2])

    def fire(self):
        if self.direction == LEFT:
            bullets.append(Bullet(texture_bullet_right, (50, 50), self.rect.x, self.rect.y, LEFT, NOT_FRIENDLY))
        elif self.direction == RIGHT:
            bullets.append(Bullet(texture_bullet_left, (50, 50), self.rect.x, self.rect.y, RIGHT, NOT_FRIENDLY))
        elif self.direction == DOWN:
            bullets.append(Bullet(texture_bullet_down, (50, 50), self.rect.x, self.rect.y, DOWN, NOT_FRIENDLY))
        elif self.direction == UP:
            bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, UP, NOT_FRIENDLY))

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
class Block(sprite.Sprite, Reset):
    def __init__(self, image_file, sprite_size, x, y, hp = 10):
        super().__init__()
        logging.info('Block created')
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = 10

#класс Unit
class Unit(sprite.Sprite, Reset):
    def __init__(self, image_file, sprite_size, x, y, direction, speed = 2, damage = 5, hp = 15):
        super().__init__()
        logging.info('Unit created')
        self.sprite_size = sprite_size
        self.image = transform.scale(image.load(image_file), self.sprite_size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.damage = 5
        self.hp = 15
        self.direction = direction

#класс Bullet
class Bullet(Unit):
    def __init__(self, image_file, sprite_size, x, y, direction, bullet_type, speed = 2, damage = 5, hp = 15):
        super().__init__(image_file, sprite_size, x, y, direction, speed, damage, hp)    
        self.bullet_type = bullet_type

    def movement(self):
        logging.info('move bullet')
        if self.direction == LEFT:
                self.rect.x -= self.speed
        elif self.direction == RIGHT:
                self.rect.x += self.speed
        elif self.direction == UP:
                self.rect.y -= self.speed
        elif self.direction == DOWN:
                self.rect.y += self.speed  

#класс Player
class Player(Unit, Change_image):

    def movement(self, group):
        #обозначение сторон хитбокса
        self.left_side = Rect(self.rect.left - 1, self.rect.top, 1, self.rect.height)
        self.right_side = Rect(self.rect.right, self.rect.top, 1, self.rect.height)
        self.top_side = Rect(self.rect.left, self.rect.top - 1, self.rect.width, 1)
        self.bottom_side = Rect(self.rect.left, self.rect.bottom, self.rect.width, 1)

        #нажатие на кнопки и движение
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and not self.left_side.collidelistall(group):
            self.change_image(texture_player1_right)
            self.direction = LEFT
            self.rect.x -= self.speed
            logging.info('move player left')
        elif keys_pressed[K_d] and not self.right_side.collidelistall(group):
            self.change_image(texture_player1_left)
            self.direction = RIGHT
            self.rect.x += self.speed
            logging.info('move player right')
        elif keys_pressed[K_w] and not self.top_side.collidelistall(group):
            self.change_image(texture_player1)
            self.direction = UP
            self.rect.y -= self.speed
            logging.info('move player up')
        elif keys_pressed[K_s] and not self.bottom_side.collidelistall(group):
            self.change_image(texture_player1_down)
            self.direction = DOWN
            self.rect.y += self.speed
            logging.info('move player down')

    def fire(self):
        global timer_for_fire
        keys_pressed = key.get_pressed()
        if keys_pressed[K_SPACE] and timer_for_fire >= 30:
            logging.info('player atack')
            if self.direction == LEFT:
                bullets.append(Bullet(texture_bullet_right, (50, 50), self.rect.x, self.rect.y, LEFT, FRIENDLY))
            elif self.direction == RIGHT:
                bullets.append(Bullet(texture_bullet_left, (50, 50), self.rect.x, self.rect.y, RIGHT, FRIENDLY))
            elif self.direction == DOWN:
                bullets.append(Bullet(texture_bullet_down, (50, 50), self.rect.x, self.rect.y, DOWN, FRIENDLY))
            elif self.direction == UP:
                bullets.append(Bullet(texture_bullet, (50, 50), self.rect.x, self.rect.y, UP, FRIENDLY))
            timer_for_fire = 0
        timer_for_fire += 1

#
#       АБСТРАКТНЫЕ КЛАССЫ
#

# Абстрактный класс врага
class Enemy(ABC, Unit, Change_image, Basic_Enemy):
    def __init__(self, image_file, sprite_size, x, y, direction, timer = 0, speed = 2, damage = 5, hp = 15):
        super().__init__(image_file, sprite_size, x, y, direction, speed, damage, hp)
        self.timer = 0
    
    @abstractmethod
    def movement(self):
        pass

# класс врага(1 уровень)
class EnemySilver(Enemy):

    def movement(self, group):  

        self.move(group, silver_tanks)

        if self.timer == 60:
            self.direction = choice((LEFT, RIGHT))
            self.timer = 0
            self.fire()
        self.timer += 1
        
# класс врага(2 уровень)       
class EnemyGold(Enemy):

    def movement(self, group):  

        self.move(group, gold_tanks)

        if self.timer == 60:
            self.direction = choice((LEFT, RIGHT, UP, DOWN))
            self.timer = 0
            self.fire()
        self.timer += 1
        
# класс врага(3 уровень)      
class EnemyDiamond(Enemy):

    def movement(self, group):  

        self.move(group, gold_tanks)

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
    

#фабрики
silver_factory = SilverEnemyFactory()
gold_factory = GoldEnemyFactory()
diamond_factory = DiamondEnemyFactory()