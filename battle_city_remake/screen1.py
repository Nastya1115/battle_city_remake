# этот модуль нужен для игрового цикла
# ! первый уровень

from classes import *

while game_run:

    for events in event.get():
        if events.type == QUIT:
            game_run = False

    try:

        window.fill((0, 0, 0))

        player.movement(block1)
        player.fire()

        for bullet in bullets:
             bullet.reset()
             bullet.movement()
             if sprite.collide_rect(bullet, block1):
                bullet.kill()

        player.reset()
        block1.reset()

    except Exception as e:
            print(str(e))

    #обновление экрана
    display.update()
    clock.tick(FPS)