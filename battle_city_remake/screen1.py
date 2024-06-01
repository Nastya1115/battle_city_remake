# этот модуль нужен для игрового цикла
# ! первый уровень

from classes import *

while game_run:

    for events in event.get():
        if events.type == QUIT:
            game_run = False

    try:

        window.fill((0, 0, 0))

        player.reset()
        player.movement()
        player.fire()

        for bullet in bullets:
             bullet.reset()
             bullet.movement()

    except Exception as e:
            print(str(e))

    #обновление экрана
    display.update()
    clock.tick(FPS)