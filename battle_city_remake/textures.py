#   это файл для импорта текстур
#
#   импорт текстур происходит примерно так:
#   мы используем для каждой текстуры свою переменную
#   texture_name = "папка1/папка2/текстура.png"


#-----------------BLOCKS-----------------
texture_block = "textures/block.png"

#-----------------BULLET-----------------
texture_bullet = "textures/bullet.png"
texture_bullet_left = "textures/bullet_left.png"
texture_bullet_right = "textures/bullet_right.png"
texture_bullet_down = "textures/bullet_down.png"

#-----------------PLAYER-----------------
player_1_up = "textures/player/player_1.png"
player_1_left = "textures/player/player_1_left.png"
player_1_right = "textures/player/player_1_right.png"
player_1_down = "textures/player/player_1_down.png"

player_2_up = "textures/player/player_2.png"
player_2_left = "textures/player/player_2_left.png"
player_2_right = "textures/player/player_2_right.png"
player_2_down = "textures/player/player_2_down.png"

player_up = [item for item in [player_1_up] * 3 + [player_2_up] * 3]
player_left = [item for item in [player_1_left] * 3 + [player_2_left] * 3]
player_down = [item for item in [player_1_down] * 3 + [player_2_down] * 3]
player_right = [item for item in [player_1_right] * 3 + [player_2_right] * 3]

#-----------------SILVER TANK-----------------
silver_tank_1_up = "textures/silver_tank/silver_tank_1.png"
silver_tank_1_left = "textures/silver_tank/silver_tank_1_left.png"
silver_tank_1_right = "textures/silver_tank/silver_tank_1_right.png"
silver_tank_1_down = "textures/silver_tank/silver_tank_1_down.png"

silver_tank_2_up = "textures/silver_tank/silver_tank_2.png"
silver_tank_2_left = "textures/silver_tank/silver_tank_2_left.png"
silver_tank_2_right = "textures/silver_tank/silver_tank_2_right.png"
silver_tank_2_down = "textures/silver_tank/silver_tank_2_down.png"

silver_tank_up = [item for item in [silver_tank_1_up] * 3 + [silver_tank_2_up] * 3]
silver_tank_left = [item for item in [silver_tank_1_left] * 3 + [silver_tank_2_left] * 3]
silver_tank_right = [item for item in [silver_tank_1_right] * 3 + [silver_tank_2_right] * 3]
silver_tank_down = [item for item in [silver_tank_1_down] * 3 + [silver_tank_2_down] * 3]

#-----------------GLOD TANK-----------------
gold_tank_1_up = "textures/gold_tank/gold_tank_1.png"
gold_tank_1_left = "textures/gold_tank/gold_tank_1_left.png"
gold_tank_1_right = "textures/gold_tank/gold_tank_1_right.png"
gold_tank_1_down = "textures/gold_tank/gold_tank_1_down.png"

gold_tank_2_up = "textures/gold_tank/gold_tank_2.png"
gold_tank_2_left = "textures/gold_tank/gold_tank_2_left.png"
gold_tank_2_right = "textures/gold_tank/gold_tank_2_right.png"
gold_tank_2_down = "textures/gold_tank/gold_tank_2_down.png"

gold_tank_up = [item for item in [gold_tank_1_up] * 3 + [gold_tank_2_up] * 3]
gold_tank_left = [item for item in [gold_tank_1_left] * 3 + [gold_tank_2_left] * 3]
gold_tank_down = [item for item in [gold_tank_1_down] * 3 + [gold_tank_2_down] * 3]
gold_tank_right = [item for item in [gold_tank_1_right] * 3 + [gold_tank_2_right] * 3]

#-----------------EXPLOSION-----------------
explosion1 = "textures/explosion1.png"
explosion2 = "textures/explosion2.png"
explosion3 = "textures/explosion3.png"
explosion4 = "textures/explosion4.png"
explosion5 = "textures/explosion5.png"
explosions = [explosion1, explosion2, explosion3, explosion4, explosion5]