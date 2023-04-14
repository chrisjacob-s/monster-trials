import random
from entity import Entity

class Hero(Entity):
  def __init__(self, name):
    ''' Passes the name and default hp to the superclass’s init '''
    super().__init__(name, 25)

  def melee_attack(self, entity):
    ''' Deals damage to the explicit entity and returns a string description of the attack '''
    # Rolls two dice and add up the value for the damage
    dice1 = random.randint(2, 6)
    dice2 = random.randint(2, 6)
    total_dmg = dice1 + dice2

    entity.take_damage(total_dmg)

    return f"{self.name} slashes the {entity.name} with their sword, dealing {total_dmg} damage."

  def ranged_attack(self, entity):
    '''Deals damage to the explicit entity and returns a string description of the attack'''
    rand_dmg = random.randint(1, 12)

    entity.take_damage(rand_dmg)

    return f"{self.name} shoots an arrow at the {entity.name}, dealing {rand_dmg} damage."