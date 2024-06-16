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
            elif quit_button.rect.collidepoint(events.pos):
                run = False
            elif settings_button.rect.collidepoint(events.pos):
                current_scene = 1
            elif continue_button.rect.collidepoint(events.pos):
                current_scene = 2
            elif exit_button.rect.collidepoint(events.pos):
                current_scene = 0
    
    try:

        scenes[current_scene].draw(window)

        if scenes[current_map].counter.killed >= 5 and current_map < len(scenes) - 1:
            current_map += 1
            current_scene += 1
        

    except Exception as e:
        print(str(e))

    display.update()
    clock.tick(FPS)

quit()