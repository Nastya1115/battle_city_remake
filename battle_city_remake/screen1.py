# этот модуль нужен для игрового цикла
# ! первый уровень

import classes

while game_run:

    for events in event.get():
        if events.type == QUIT:
            game_run = False

    #обновление экрана
    display.update()
    clock.tick(FPS)