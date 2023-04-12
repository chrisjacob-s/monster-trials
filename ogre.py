# Justin
import random
from entity import Entity

class EasyOgre(Entity):
  def __init__(self):
    super().__init__("Sleepy Ogre", random.randint(7, 8))

  def melee_attack(self, entity):
    rand_dmg = random.randint(5, 8)

    entity.take_damage(rand_dmg)