import pygame

(DIRECTION_UP, DIRECTION_DOWN, DIRECTION_RIGHT, DIRECTION_LEFT) = range(4)
DISPLAY = pygame.Surface((200, 200))

class Bullet:
    def __init__(self, direction=DIRECTION_UP,
                 position = None):
        self.x = position[0]
        self.y = position[1]
        self.speed = 2
        self.direction = direction
        self.kind = kind
        self.rect = pygame.Rect(self.x, self.y, 4, 4)
        self.image = BULLET_IMAGES[self.direction]
        self.owner = owner
        self.level = level
        self.image = pygame.image.load('tank.png')

    def fly(self):
        if (0 < self.rect.x < DISPLAY.get_width() - self.image.get_width() and
                (0 < self.rect.y < DISPLAY.get_height() -
                 self.image.get_height())):
            if self.direction == DIRECTION_LEFT:
                self.x -= self.speed
            if self.direction == DIRECTION_RIGHT:
                self.x += self.speed
            if self.direction == DIRECTION_UP:
                self.y -= self.speed
            if self.direction == DIRECTION_DOWN:
                self.y += self.speed
            self.rect.topleft = round(self.x), round(self.y)
            for tile in get_hit_list(self.rect, self.level.game_map):
                if tile.type == BRICK:
                    self.level.kill_tile(tile)
                if tile.type == BETON and self.kind == 1:
                    self.level.kill_tile(tile)
                if tile.type not in {GRASS, WATER}:
                    self.die()
                elif tile.type in {WATER}:
                    self.level.game.draw(self)
            
        else:
            self.die()

    def die(self):
        if self in self.level.bullets:
            self.level.explosions.append(Explosion(self.rect.topleft, 0))
            self.level.bullets.remove(self)
            self.owner.current_bullets += 1

class Tank:
    def __init__(self, health, speed, pos, direction=DIRECTION_UP,):
        self.x = position[0]
        self.y = position[1]
        self.speed = speed
        self.image = pygame.image.load('tank.png')
        self.direction = direction
        self.health = health
        self.pos = pos

    def fire(self):
        
        if self.direction == DIRECTION_UP:
            self.level.bullets.append(Bullet(self.bullet_type,
                                                self.direction,
                                                (self.rect.x + 5,
                                                self.rect.y),
                                                self, self.level))
        if self.direction == DIRECTION_DOWN:
            self.level.bullets.append(Bullet(self.bullet_type,
                                                self.direction,
                                                (self.rect.x + 5,
                                                self.rect.y + 12),
                                                self, self.level))
        if self.direction == DIRECTION_RIGHT:
            self.level.bullets.append(Bullet(self.bullet_type,
                                                self.direction,
                                                (self.rect.x + 12,
                                                self.rect.y + 6),
                                                self, self.level))
        if self.direction == DIRECTION_LEFT:
            self.level.bullets.append(Bullet(self.bullet_type,
                                                self.direction,
                                                (self.rect.x,
                                                self.rect.y + 6),
                                                self, self.level))
          
    def movement(self):
        if event.type == pygame.event.get:
            if event.key == pygame.KeyA:
                if self.direction == DIRECTION_LEFT:
                    self.x -= self.speed

        if event.type == pygame.event.get:
            if event.key == pygame.KeyD:
                if self.direction == DIRECTION_RIGHT:
                    self.x += self.speed

        if event.type == pygame.event.get:
            if event.key == pygame.KeyW:
                if self.direction == DIRECTION_UP:
                    self.y -= self.speed

        if event.type == pygame.event.get:
            if event.key == pygame.KeyS:
                if self.direction == DIRECTION_DOWN:
                    self.y += self.speed
        self.rect.topleft = round(self.x), round(self.y)
    
    def collide_with_bonus(self, bonus):
        if self.colliderect(bonus):
            if bonus_type == SPEED:
                self.speed += 1
                    

