import random
from entity import Entity

class EasyTroll(Entity):
  def __init__(self):
    super().__init__("Juvenile Troll", random.randint(5, 7))

  def melee_attack(self, entity):
    rand_dmg = random.randint(4, 6)

    entity.take_damage(rand_dmg)