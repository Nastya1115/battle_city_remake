# этот модуль нужен для игрового цикла
# ! первый уровень

from classes import *

while game_run:

    for events in event.get():
        if events.type == QUIT:
            game_run = False

    try:

        player.reset()

    except Exception as e:
            print(str(e))

    #обновление экрана
    display.update()
    clock.tick(FPS)