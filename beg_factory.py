import random
from enemy_factory import EnemyFactory
from easy_goblin import EasyGoblin
from easy_troll import EasyTroll
from easy_ogre import EasyOgre

class BeginnerFactory(EnemyFactory):
  def create_random_enemy(self):
    rand_enemy = random.randint(1, 3)

    if rand_enemy == 1:
      return EasyGoblin()
    elif rand_enemy == 2:
      return EasyTroll()
    elif rand_enemy == 3:
      return EasyOgre()
