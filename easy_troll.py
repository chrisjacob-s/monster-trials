import random
from entity import Entity

class EasyTroll(Entity):
  def __init__(self):
    ''' Using super, gives each monster a default name and randomize its hp '''
    super().__init__("Juvenile Troll", random.randint(5, 7))

  def melee_attack(self, entity):
    ''' Randomizes the damage, deals the damage to the explicit entity, and returns a string describing the attack '''
    rand_dmg = random.randint(4, 6)

    entity.take_damage(rand_dmg)

    return f"{self.name} fiercely claws {entity.name}, dealing {rand_dmg} damage."