import random
from entity import Entity

class EasyOgre(Entity):
  def __init__(self):
    ''' Using super, gives each monster a default name and randomize its hp '''
    super().__init__("Sleepy Ogre", random.randint(7, 8))

  def melee_attack(self, entity):
    ''' Randomizes the damage, deals the damage to the explicit entity, and returns a string describing the attack '''
    rand_dmg = random.randint(5, 8)

    entity.take_damage(rand_dmg)

    return f"{self.name} winds up its' fist and punches {entity.name}, dealing {rand_dmg} damage."