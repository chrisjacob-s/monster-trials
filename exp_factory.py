import random
import enemy_factory
import goblin
import ogre
import troll

class ExpertFactory(enemy_factory.EnemyFactory):
  """
    A class that represents an expert factory that can create a random enemy from a list of available enemy types.

    Inherits from:
    EnemyFactory

    Attributes:
    Inherits all attributes from EnemyFactory class
    """
  def create_random_enemy(self):
    """
    Creates a random enemy object from a list of available enemy types.
    """
    enemy = [goblin.Goblin(),ogre.Ogre(),troll.Troll()]
    expert_enemy = random.choice(enemy)
    return expert_enemy