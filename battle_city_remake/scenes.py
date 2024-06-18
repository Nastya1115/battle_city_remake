from map import *

#создание кнопок
play_button = ImageButton(WIN_SIZE[0]/2 - 100, 270, 202, 83, "", "textures/buttons/play.png")
quit_button = ImageButton(WIN_SIZE[0]/2 - 100, 420, 202, 83, "", "textures/buttons/exit.png")
settings_button = ImageButton(0, 0, 150, 55, "", "textures/buttons/pause.png")
continue_button = ImageButton(550, 500, 282, 83, "", "textures/buttons/continue.png")
exit_button = ImageButton(0, 500, 202, 83, "", "textures/buttons/home.png")
quit_button_for_game_over_and_win = ImageButton(600, 500, 200, 83, "", "textures/buttons/exit.png")
restart_button = ImageButton(300, 500, 202, 83, "", "textures/buttons/replay.png")


# создание фона
main_fon = transform.scale(image.load("textures/fons/play_1.png"), (250,250))
game_over_fon = transform.scale(image.load("textures/fons/game_over_fon.png"), (250,250))
win_fon = transform.scale(image.load("textures/fons/win_fon.png"), (250,250))


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
        window.blit(main_fon, (280,0))
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

class Game_Over(Scene):
    def __init__(self):
        self.restart_button = restart_button
        self.exit_button = exit_button
        self.quit_button_for_game_over_and_win = quit_button_for_game_over_and_win

    
    def draw(self, window):
        window.fill(GAME_SCREEN)
        window.blit(game_over_fon, (300,100))
        music_play(finish_sound, 0.1)
        self.exit_button.draw(window)
        self.restart_button.draw(window)
        self.quit_button_for_game_over_and_win.draw(window)
      
class Win(Scene):
    def __init__(self):
        self.finish_screen_win = GAME_SCREEN
        self.exit_button = exit_button
        self.restart_button = restart_button
        self.quit_button_for_game_over_and_win = quit_button_for_game_over_and_win

    
    def draw(self, window):
        window.fill(self.finish_screen_win)
        window.blit(win_fon, (300,100))
        music_play(default_sound, 0.1)
        self.exit_button.draw(window)
        self.restart_button.draw(window)
        self.quit_button_for_game_over_and_win.draw(window)

class Level(Scene):
    def __init__(self, level, factories_type, goal):
        self.level = level
        self.player = None
        self.blocks = []
        self.enemies = []
        self.factories_type = factories_type
        self.goal = goal
        self.Map_generation(level)

    def factories_type_list(self, factories_type):
        choice(factories_type)

    def Map_generation(self, level):
        self.counter = Counter()
        #перебор массива
        for y, row in enumerate(level):
            y *= PIXEL
            for x, type in enumerate(row):
                x *= PIXEL

                #игрок
                if type == 'p':
                    self.player = Player(x, y, player_1_right, SPRITE_SIZE, RIGHT, 20)
                    logging.info('Player created')

                #враги - рандом
                elif type == 'e':
                    self.enemies.append(choice(self.factories_type).create_enemy(x, y, silver_tank_1_right, SPRITE_SIZE, RIGHT, 5))

                #блок
                elif type == 'b':
                    self.blocks.append(Block(x, y, texture_block, SPRITE_SIZE))
        self.enemies_count = len(self.enemies)

    def reset_level(self, level):
        self.player = None
        self.blocks.clear()
        self.enemies.clear()
        bullets.clear()
        effects.clear()
        self.enemies_count = 0
        self.Map_generation(level)

    def draw(self, window):
        window.fill(GAME_SCREEN)

        #перезагрузка пуль
        for bullet in bullets:
            bullet.movement()
            bullet.reset()

            #проверка на столкновение пуль с обьектами
            #проверка пули и игрока
            if bullet.rect.colliderect(self.player) and bullet.bullet_type == NOT_FRIENDLY and bullet in bullets:
                if self.player.hp >= 1:
                    bullets.remove(bullet)
                    self.player.hp -= bullet.damage  
                elif self.player.hp <= 0:
                    bullets.remove(bullet)
            #проверка пули и блоков
            elif bullet.rect.collidelistall(self.blocks) and bullet in bullets:
                bullets.remove(bullet)
            #проверка пули и врага
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy) and bullet.bullet_type == FRIENDLY and bullet in bullets:
                    if enemy.hp >= 1:
                        bullets.remove(bullet)
                        enemy.hp -= bullet.damage
                    elif enemy.hp <= 0 and enemy in self.enemies:
                        bullets.remove(bullet)
                        self.enemies.remove(enemy)
                        music_play(explosion_sound, 0.5)
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
                self.enemies.append(choice(self.factories_type).create_enemy(x, y, silver_tank_1_right, SPRITE_SIZE, RIGHT, 5))
            block.reset()

        for effect in effects:
            effect.reset()
            effect.animation()
            
        self.counter.reset(self.player, self.goal)
        settings_button.draw(window)




menu = Menu()
pause = Pause()
win = Win()
game_over = Game_Over()
level1 = Level(level_1, [silver_factory], 5)
level2 = Level(level_2, [silver_factory, gold_factory], 10)

current_scene = 0
current_map = 4
lvls = [level1, level2]
maps = [level_1, level_2]
scenes = [menu, pause, win, game_over, level1, level2]