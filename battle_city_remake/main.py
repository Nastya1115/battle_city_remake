# ! основное игровое меню
# здесь будут обьеденяться уровни и менюшка

from start import *

# Основные переменные
game_in_system = True
just_game = False
in_menu = False
paused = False
        
        
class ImageButton:
    def __init__(self, x, y, width, height, text, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self.image = image.load(image_path)
        self.image = transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  #создание прямоугольной области с размерами изображения

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
            
            
# Основные цвета
Main_screen = (255, 0, 0)
Game_screen = (255, 255, 255)
settings_screen  = (128, 128, 128)
# создание кнопок
play_button = ImageButton(WIN_SIZE[0]/2 - 100, 120, 202, 83, "", "textures/182.png")
quit_button = ImageButton(WIN_SIZE[0]/2 - 100, 270, 202, 83, "", "textures/181.png")
settings_button = ImageButton(0, 0, 202, 83, "", "textures/183.png")
continue_button = ImageButton(500, 500, 282, 83, "", "textures/184.png")
exit_button = ImageButton(0, 500, 202, 83, "", "textures/185.png")

# настройки шрифта
font = font.Font(None, 36)
text_font = font.render("Main screen", True, (255,255,255))
text_rect = text_font.get_rect(center=(400,50))

# Основной цикл
while game_in_system:
    for events in event.get():
        if events.type == QUIT:
            game_in_system = False
    
        if events.type == MOUSEBUTTONDOWN:
            if play_button.rect.collidepoint(events.pos):
                just_game = True
                in_menu = False
            elif quit_button.rect.collidepoint(events.pos):
                game_in_system = False
            elif settings_button.rect.collidepoint(events.pos):
                paused = True
            elif continue_button.rect.collidepoint(events.pos):
                just_game = True
                paused = False
            elif exit_button.rect.collidepoint(events.pos):
                in_menu = True
                paused = False

    window.fill(Main_screen)
    play_button.draw(window)
    quit_button.draw(window)
    window.blit(text_font, text_rect)

    if just_game:
        window.fill(Game_screen)
        game_text_font = font.render("Тут типо игра", True, (0,0,0))
        game_text_rect = game_text_font.get_rect(center=(WIN_SIZE[0]/2, WIN_SIZE[1]/2))
        settings_button.draw(window)
        window.blit(game_text_font, game_text_rect)
        
    if paused:
        window.fill(settings_screen)
        game_text_font = font.render("Настройки", True, (50,50,50))
        game_text_rect = game_text_font.get_rect(center=(WIN_SIZE[0]/2, WIN_SIZE[1]/2))
        continue_button.draw(window)
        exit_button.draw(window)
        window.blit(game_text_font, game_text_rect)
    
    if in_menu:
        window.fill(Main_screen)
        play_button.draw(window)
        quit_button.draw(window)
        window.blit(text_font, text_rect)

        
    
    display.flip()

quit()