import abc

class Entity(abc.ABC):
  def __init__(self, name, hp):
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
    self._hp -= dmg

    if self._hp < 0:
      self._hp = 0

  def __str__(self):
    return f"{self._name} HP: {self._hp}"

  @abc.abstractmethod
  def melee_attack(self, entity):
    pass