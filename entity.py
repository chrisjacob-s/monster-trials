import abc

class Entity(abc.ABC):
  def __init__(self, name, hp):
    ''' Represents the name and hp of the entity
    Attributes:
      _name (str): name of entity
      _hp (int): health points of entity
    '''
    self._name = str(name)
    self._hp = int(hp)

  # Decorator for get
  @property
  def name(self):
    ''' Returns name of entity '''
    return self._name

  # Decorator for get
  @property
  def hp(self):
    ''' Returns hp of entity '''
    return self._hp

  def take_damage(self, dmg):
    ''' Deals the damage the entity takes '''
    self._hp -= dmg

    # If entity's health goes below 0, reset it to 0
    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    ''' Return a string with the entity’s name and hp '''
    return f"{self._name} HP: {self._hp}"

  @abc.abstractmethod
  def melee_attack(self, entity):
    ''' The attack the entity does to another entity '''
    pass