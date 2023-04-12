import abc

class EnemyFactory(abc.ABC):
  @abc.abstractmethod
  def create_random_enemy(self):
    ''' Template for all enemy factories '''
    pass