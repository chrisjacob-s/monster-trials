# Christopher Soriano and Justin Donate
# 4/11/23
#

import check_input
from hero import Hero
from beg_factory import BeginnerFactory

def main():
  print("Monster Trials\n")

  name = input("What is your name hero? ")
  player = Hero(name)
  print("")

  print(f"You will face a series of 3 monsters, {player.name}.")
  print("Defeat them all to win.\n")

  print("Difficulty:\n1. Beginner\n2. Expert")
  difficulty = check_input.get_int_range("", 1, 2)

  if difficulty == 1:
    beg_enemies = BeginnerFactory()

    

  # TESTING
  # e = Hero("Enemy")
  # h = Hero("Chris")
  # print(h)
  # print(e)
  # print("Hero swings his sword at Enemy")
  # h.melee_attack(e)
  # print(e)
  # print("Enemy shoots an arrow at Hero")
  # e.ranged_attack(h)
  # print(h)
  # factory = BeginnerFactory()
  # print(factory.create_random_enemy())
  # TESTING

main()