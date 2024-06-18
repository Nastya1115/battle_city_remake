from scenes import *


run = True
while run:
    
    for events in event.get():
        if events.type == QUIT:
            run = False
            
        #нажатие на кнопок в меню
        if events.type == MOUSEBUTTONDOWN:
            if play_button.rect.collidepoint(events.pos):
                current_scene = current_map
            elif quit_button.rect.collidepoint(events.pos) or quit_button_for_game_over_and_win.rect.collidepoint(events.pos):
                run = False
            elif settings_button.rect.collidepoint(events.pos):
                current_scene = 1
            elif continue_button.rect.collidepoint(events.pos):
                current_scene = current_map
                print('1')
            elif exit_button.rect.collidepoint(events.pos):
                current_map = 4
                scenes[current_map].reset_level(scenes[current_map].level)
                current_scene = 0
            elif restart_button.rect.collidepoint(events.pos):
                current_scene = current_map
    
    try:

        scenes[current_scene].draw(window)

        if current_scene >= 4:
            lvl_counter = current_scene - 3
            level_counter = font.render(f"Уровень: {lvl_counter}", True, (255,255,255))     
            window.blit(level_counter, (WIN_SIZE[0] - 155, 60))

        if scenes[current_map].counter.killed >= scenes[current_map].goal and current_map < len(scenes) - 1:
            current_map += 1
            current_scene += 1

        elif scenes[current_map].counter.killed >= scenes[current_map].goal and current_map >= len(scenes) - 1:
            for lvl in lvls:
                lvl.reset_level(maps[lvls.index(lvl)])
            current_map = 4
            current_scene = 2

        elif scenes[current_map].player.hp <= 0:
            for lvl in lvls:
                lvl.reset_level(maps[lvls.index(lvl)])
            current_map = 4
            current_scene = 3
        

    except Exception as e:
        print(str(e))

    display.update()
    clock.tick(FPS)

quit()