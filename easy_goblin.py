import random
from entity import Entity

class EasyGoblin(Entity):
  def __init__(self):
    super().__init__("Scrawny Goblin", random.randint(6, 9))

  def melee_attack(self, entity):
    rand_dmg = random.randint(5, 9)

    entity.take_damage(rand_dmg)