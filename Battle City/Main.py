import pygame
pygame.init()

# Создаем окно
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TEST")

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

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))  #создание прямоугольной области с размерами изображения

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
            
            
# Основные цвета
Main_screen = (255, 0, 0)
Game_screen = (255, 255, 255)
settings_screen  = (128, 128, 128)
# создание кнопок
play_button = ImageButton(WIDTH/2 - 100, 120, 202, 83, "", "182.png")
quit_button = ImageButton(WIDTH/2 - 100, 270, 202, 83, "", "181.png")
settings_button = ImageButton(0, 0, 202, 83, "", "183.png")
continue_button = ImageButton(500, 500, 282, 83, "", "184.png")
exit_button = ImageButton(0, 500, 202, 83, "", "185.png")

# настройки шрифта
font = pygame.font.Font(None, 36)
text_font = font.render("Main screen", True, (255,255,255))
text_rect = text_font.get_rect(center=(400,50))

# Основной цикл
while game_in_system:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_in_system = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.rect.collidepoint(event.pos):
                just_game = True
                in_menu = False
            elif quit_button.rect.collidepoint(event.pos):
                game_in_system = False
            elif settings_button.rect.collidepoint(event.pos):
                paused = True
            elif continue_button.rect.collidepoint(event.pos):
                just_game = True
                paused = False
            elif exit_button.rect.collidepoint(event.pos):
                in_menu = True
                paused = False

    screen.fill(Main_screen)
    play_button.draw(screen)
    quit_button.draw(screen)
    screen.blit(text_font, text_rect)

    if just_game:
        screen.fill(Game_screen)
        game_text_font = font.render("Тут типо игра", True, (0,0,0))
        game_text_rect = game_text_font.get_rect(center=(WIDTH/2, HEIGHT/2))
        settings_button.draw(screen)
        screen.blit(game_text_font, game_text_rect)
        
    if paused:
        screen.fill(settings_screen)
        game_text_font = font.render("Настройки", True, (50,50,50))
        game_text_rect = game_text_font.get_rect(center=(WIDTH/2, HEIGHT/2))
        continue_button.draw(screen)
        exit_button.draw(screen)
        screen.blit(game_text_font, game_text_rect)
    
    if in_menu:
        screen.fill(Main_screen)
        play_button.draw(screen)
        quit_button.draw(screen)
        screen.blit(text_font, text_rect)

        
    
    pygame.display.flip()

pygame.quit()
