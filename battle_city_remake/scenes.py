from map import *


#создание кнопок
play_button = ImageButton(WIN_SIZE[0]/2 - 100, 120, 202, 83, "", "textures/buttons/play.png")
quit_button = ImageButton(WIN_SIZE[0]/2 - 100, 270, 202, 83, "", "textures/buttons/quit.png")
settings_button = ImageButton(0, 0, 150, 55, "", "textures/buttons/settings.png")
continue_button = ImageButton(250, 400, 282, 83, "", "textures/buttons/continue.png")
exit_button = ImageButton(0, 400, 202, 83, "", "textures/buttons/exit.png")


#отдельный абстрактный класс Scene
class Scene(ABC):

    @abstractmethod
    def draw(self, window):
        pass

class Menu(Scene):
    def __init__(self):
        self.main_screen = MAIN_SCREEN
        self.play_button = play_button
        self.quit_button = quit_button
        self.text_font = text_font
        self.text_rect = text_rect
    
    def draw(self, window):
        window.fill(self.main_screen)
        self.play_button.draw(window)
        self.quit_button.draw(window)
        window.blit(self.text_font, self.text_rect)

class Pause(Scene):
    def __init__(self):
        self.settings_screen = SETTINGS_SCREEN
        self.continue_button = continue_button
        self.exit_button = exit_button
    
    def draw(self, window):
        window.fill(self.settings_screen)
        game_text_font = font.render("Настройки", True, (50,50,50))
        game_text_rect = game_text_font.get_rect(center=(WIN_SIZE[0] // 2, WIN_SIZE[1] // 2))
        self.continue_button.draw(window)
        self.exit_button.draw(window)
        window.blit(game_text_font, game_text_rect)
                            
class Level(Scene):
    def __init__(self, level):
        self.level = level
        self.player = None
        self.blocks = []
        self.enemies = []
        self.Map_generation(level)
        
    def Map_generation(self, level):
        self.counter = Counter()
        #перебор массива
        for y, row in enumerate(level):
            y *= PIXEL
            for x, type in enumerate(row):
                x *= PIXEL

                #игрок
                if type == 'p':
                    self.player = Player(x, y, player_1_up, SPRITE_SIZE, RIGHT)

                #враг
                elif type == 'e':
                    self.enemies.append(choice(((silver_factory.create_enemy(x, y, silver_tank_1_left, SPRITE_SIZE, RIGHT)), (gold_factory.create_enemy(x, y, gold_tank_1_up, SPRITE_SIZE, RIGHT)))))

                #блок
                elif type == 'b':
                    self.blocks.append(Block(x, y, texture_block, SPRITE_SIZE))
        self.enemies_count = len(self.enemies)

    def draw(self, window):
        window.fill(GAME_SCREEN)

        #перезагрузка пуль
        for bullet in bullets:
            bullet.movement()
            bullet.reset()

            #проверка на столкновение пуль с обьектами
            #проверка пули и игрока
            if bullet.rect.colliderect(self.player) and bullet.bullet_type == NOT_FRIENDLY:
                if self.player.hp >= 1:
                    bullets.remove(bullet)
                    self.player.hp -= bullet.damage  
                elif self.player.hp <= 0:
                    bullets.remove(bullet)
            #проверка пули и блоков
            elif bullet.rect.collidelistall(self.blocks):
                bullets.remove(bullet)
            #проверка пули и врага
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy) and bullet.bullet_type == FRIENDLY:
                    if enemy.hp >= 1:
                        bullets.remove(bullet)
                        enemy.hp -= bullet.damage
                    elif enemy.hp <= 0:
                        bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        self.counter.killed += 1
                        effects.append(Explosion(enemy.rect.x, enemy.rect.y))

        #перезагрузка врага

        for enemy in self.enemies:
            enemy.movement(self.blocks)
            enemy.reset()

        #перезагрузка игрока
        self.player.movement(self.blocks)
        self.player.fire()
        self.player.reset()

        #перезагрузка блоков
        for block in self.blocks:
            x = randint(0, WIN_SIZE[0] - SPRITE_SIZE[0])
            y = randint(0, WIN_SIZE[1]  - SPRITE_SIZE[1])
            help_rect = Rect(x, y, SPRITE_SIZE[0], SPRITE_SIZE[1])
            if len(self.enemies) < self.enemies_count and not help_rect.collidelistall(self.blocks):
                self.enemies.append(choice(((silver_factory.create_enemy(x, y, silver_tank_1_left, SPRITE_SIZE, RIGHT)), (gold_factory.create_enemy(x, y, gold_tank_1_up, SPRITE_SIZE, RIGHT)))))
            block.reset()

        for effect in effects:
            effect.reset()
            effect.animation()
            
        self.counter.reset(self.player)
        settings_button.draw(window)


menu = Menu()
pause = Pause()
level1 = Level(level_1)
level2 = Level(level_2)

current_scene = 0
current_map = 2
maps = [level1, level2]
scenes = [menu, pause, level1, level2]