from main import *

# созадние теста для игровой логики(TestGameLogic)
class TGL(unittest.TestCase):
    #инициализруем game, player, enemy
    def setUp(self):
        self.game = game_in_system
        self.player = Player()
        self.enemy = Enemy()
    # Проверка урона от врага к игроку       
    def test_player_damage_from_enemy(self):
        player_health = self.player.hp
        self.enemy.collide_with(self.player) #Обработка последствий столкновения
        self.assertLess(self.player.hp, player_health) # assertLess нужен для проверки, что первый аргумент меньше второго.
      # Проверка урона от игрока к врагу 
    def test_enemy_damage_from_player(self):
        enemy_health = self.enemy.hp
        self.bullet.collide_with(self.enemy)
        self.assertLess(self.enemy.hp, enemy_health)
        
    # Проверка движения врага в сторону игрока
    def test_enemy_movement_towards_player(self):
        enemy_position = self.enemy.position
        self.enemy.move_towards(self.player) #move_towards нужен для перемещения объекта в сторону другой точки или объекта
        self.assertNotEqual(self.enemy.position, enemy_position) # метод  assertNotEqual используемый для проверки, что два значения не равны
        
    # Проверка движения игрока в сторону врага
    def test_player_movement_towards_enemy(self):
        player_position = self.enemy.position
        self.player.move_towards(self.enemy)
        self.assertNotEqual(self.player.position, player_position)
        

class TestGameScenes(unittest.TestCase):
    #инициализруем game
    def setUp(self):
        self.game = game_in_system
    # Проверка начального состояния игры 
    def test_start_game_state(self):
        self.assertTrue(self.game.in_menu)
        self.assertFalse(self.game.lvl_1)
        self.assertFalse(self.game.paused)

    # Проверка запуска игры из главного меню
    def test_game_start_from_menu(self):
        self.game.in_menu = True
        self.game.handle_mouse_click(WIN_SIZE[0]/2 - 100, 120)
        self.assertTrue(self.game.lvl_1)
        self.assertFalse(self.game.in_menu)
        
    def test_game_pause(self):
        # Проверка перехода в режим паузы
        self.game.lvl_1 = True
        self.game.handle_mouse_click(0, 0)
        self.assertTrue(self.game.paused)
        self.assertFalse(self.game.lvl_1)
        
if __name__ == '__main__':
    unittest.main()
        
