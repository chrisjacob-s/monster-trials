import random
from entity import Entity

class Ogre(Entity):
  '''
    A class representing a ogre entity that can use blood magic and deal melee attacks to other entities.

    Inherits from:
    Entity

    Attributes:
    Inherits all attributes from Entity class.
'''
  def __init__(self):
    '''creates an instance of Ogre with a name and a random health points'''
    super().__init__("Giant Ogre", random.randint(8, 12))

  def melee_attack(self, entity):
     '''Performs a melee attack on the input entity and decreases its health points.'''
    rand_dmg = random.randint(6, 10)

    entity.take_damage(rand_dmg)

    return f"{self.name} bawls up its' fists and smashes {entity.name}, dealing {rand_dmg} damage."