import random
from entity import Entity

class Hero(Entity):
  def __init__(self, name):
    super().__init__(name, 25)

  def melee_attack(self, entity):
    rand_dmg = random.randint(2, 6)

    entity.take_damage(rand_dmg)

  def ranged_attack(self, entity):
    rand_dmg = random.randint(1, 12)

    entity.take_damage(rand_dmg)