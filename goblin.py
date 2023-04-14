import random
from entity import Entity

class Goblin(Entity):
  '''
    A class representing a Goblin entity that can use blood magic and deal melee attacks to other entities.

    Inherits from:
    Entity

    Attributes:
    Inherits all attributes from Entity class.
'''
  def __init__(self):
    '''creates an instance of Goblin with a name and a random health points'''
    super().__init__("Night Goblin", random.randint(6, 10))

  def melee_attack(self, entity):
    '''Performs a melee attack on the input entity and decreases its health points.'''
    rand_dmg = random.randint(5, 8)

    entity.take_damage(rand_dmg)

    return f"{self.name} sneaks behind {entity.name} and stabs them, dealing {rand_dmg} damage."