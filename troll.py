import random
from entity import Entity

class Troll(Entity):
  '''
    A class representing a troll entity that can use blood magic and deal melee attacks to other entities.

    Inherits from:
    Entity

    Attributes:
    Inherits all attributes from Entity class.
'''
  
  def __init__(self):
    '''creates an instance of Troll with a name and a random health points'''
    super().__init__("Blood Troll", random.randint(10, 14))

  def melee_attack(self, entity):
    '''Performs a melee attack on the input entity and decreases its health points.'''
    rand_dmg = random.randint(8, 12)

    entity.take_damage(rand_dmg)

    return f"{self.name} uses blood magic and blasts {entity.name}, dealing {rand_dmg} damage."