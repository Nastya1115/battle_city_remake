# ! основное игровое меню
# здесь будут обьеденяться уровни и менюшка

from map import *

# Основные переменные
game_in_system = True
lvl_1 = False
in_menu = False
paused = False            
            
# Основные цвета
Main_screen = (255, 0, 0)
Game_screen = (0, 0, 0)
settings_screen  = (128, 128, 128)

# создание кнопок
play_button = ImageButton(WIN_SIZE[0]/2 - 100, 120, 202, 83, "", "textures/182.png")
quit_button = ImageButton(WIN_SIZE[0]/2 - 100, 270, 202, 83, "", "textures/181.png")
settings_button = ImageButton(0, 0, 150, 55, "", "textures/183.png")
continue_button = ImageButton(250, 400, 282, 83, "", "textures/184.png")
exit_button = ImageButton(0, 400, 202, 83, "", "textures/185.png")

# настройки шрифта
font = font.Font(None, 36)
text_font = font.render("Main screen", True, (255,255,255))
text_rect = text_font.get_rect(center=(400,50))

# Основной цикл
while game_in_system:
    for events in event.get():
        if events.type == QUIT:
            game_in_system = False
            
        #нажатие на кнопок в меню
        if events.type == MOUSEBUTTONDOWN:
            if play_button.rect.collidepoint(events.pos):
                lvl_1 = True
                in_menu = False
            elif quit_button.rect.collidepoint(events.pos):
                game_in_system = False
            elif settings_button.rect.collidepoint(events.pos):
                paused = True
            elif continue_button.rect.collidepoint(events.pos):
                lvl_1 = True
                paused = False
            elif exit_button.rect.collidepoint(events.pos):
                in_menu = True
                paused = False

    try:
        #основное меню
        window.fill(Main_screen)
        play_button.draw(window)
        quit_button.draw(window)
        window.blit(text_font, text_rect)

        #уровень 1
        if lvl_1:
            
            window.fill(Game_screen)

            #перезагрузка пуль
            for bullet in bullets:
                bullet.movement()
                bullet.reset()

                #проверка на столкновение пуль с обьектами
                #проверка пули и игрока
                if bullet.rect.colliderect(player) and bullet.bullet_type == NOT_FRIENDLY:
                    if player.hp >= 1:
                        bullets.remove(bullet)
                        player.hp -= bullet.damage  
                    elif player.hp <= 0:
                        bullets.remove(bullet)
                #проверка пули и блоков
                elif bullet.rect.collidelistall(blocks):
                    bullets.remove(bullet)
                #проверка пули и врага
                for enemy in enemies:
                    if bullet.rect.colliderect(enemy) and bullet.bullet_type == FRIENDLY:
                        if enemy.hp >= 1:
                            bullets.remove(bullet)
                            enemy.hp -= bullet.damage
                        elif enemy.hp <= 0:
                            bullets.remove(bullet)
                            enemies.remove(enemy)

            #перезагрузка врага
            for enemy in enemies:
                enemy.movement(blocks)
                enemy.reset()

            #перезагрузка игрока
            player.movement(blocks)
            player.fire()
            player.reset()

            #перезагрузка блоков
            for block in blocks:
                block.reset()

            settings_button.draw(window)
            
        #пауза
        if paused:
            window.fill(settings_screen)
            game_text_font = font.render("Настройки", True, (50,50,50))
            game_text_rect = game_text_font.get_rect(center=(WIN_SIZE[0]/2, WIN_SIZE[1]/2))
            continue_button.draw(window)
            exit_button.draw(window)
            window.blit(game_text_font, game_text_rect)
        
        #меню
        if in_menu:
            window.fill(Main_screen)
            play_button.draw(window)
            quit_button.draw(window)
            window.blit(text_font, text_rect)

        
    #хз как назвать
    except Exception as e:
        print(str(e))
    display.update()
    clock.tick(FPS)
    
quit()