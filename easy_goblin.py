import random
from entity import Entity

class EasyGoblin(Entity):
  def __init__(self):
    ''' Using super, gives each monster a default name and randomize its hp '''
    super().__init__("Scrawny Goblin", random.randint(6, 9))

  def melee_attack(self, entity):
    ''' Randomizes the damage, deals the damage to the explicit entity, and returns a string describing the attack '''
    rand_dmg = random.randint(5, 9)

    entity.take_damage(rand_dmg)

    return f"{self.name} hungrily bites {entity.name}, dealing {rand_dmg} damage."