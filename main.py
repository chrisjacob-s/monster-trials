# Christopher Soriano and Justin Donate
# 4/11/23
# The program allows the player to fight against three different types of monsters (Goblin, Troll, and Ogre). They can adjust the difficulty 

import check_input
from hero import Hero
from beg_factory import BeginnerFactory
from exp_factory import ExpertFactory

def main():
  print("Monster Trials\n")

  print("Welcome to the Monster Trials!")
  name = input("What is your name hero? ")
  player = Hero(name)
  print("")

  print(f"You will face a series of 3 monsters, {player.name}.")
  print("Defeat them all to win.\n")

  print("Difficulty:\n1. Beginner\n2. Expert")
  difficulty = check_input.get_int_range("", 1, 2)

  # Beginner Enemies
  if difficulty == 1:
    exp_enemies = BeginnerFactory()
    enemy_list = [exp_enemies.create_random_enemy(), exp_enemies.create_random_enemy(), exp_enemies.create_random_enemy()]

    # Continue battling until player defeats all enemies
    while len(enemy_list) != 0:
      print("")
      print("Choose an enemy to attack.")
      if len(enemy_list) == 3:
        print(f"1. {enemy_list[0]}")
        print(f"2. {enemy_list[1]}")
        print(f"3. {enemy_list[2]}")
      elif len(enemy_list) == 2:
        print(f"1. {enemy_list[0]}")
        print(f"2. {enemy_list[1]}")
      elif len(enemy_list) == 1:
        print(f"1. {enemy_list[0]}")
      who_to_attack = check_input.get_int_range("", 1, len(enemy_list))
  
      print("")
      if who_to_attack == 1:
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        hero_attack = check_input.get_int_range("", 1, 2)
        print("")
        if hero_attack == 1:
          print(player.melee_attack(enemy_list[0]))
        elif hero_attack == 2:
          print(player.ranged_attack(enemy_list[0]))
  
        if enemy_list[0].hp == 0:
          print(f"{enemy_list[0].name} has fallen.")
          enemy_list.pop(0)
        else:
          print(enemy_list[0].melee_attack(player))
      elif who_to_attack == 2:
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        hero_attack = check_input.get_int_range("", 1, 2)
        print("")
        if hero_attack == 1:
          print(player.melee_attack(enemy_list[1]))
        elif hero_attack == 2:
          print(player.ranged_attack(enemy_list[1]))
        
        if enemy_list[1].hp == 0:
          print(f"{enemy_list[1].name} has fallen.")
          enemy_list.pop(1)
        else:
          print(enemy_list[0].melee_attack(player))
      elif who_to_attack == 3:
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        hero_attack = check_input.get_int_range("", 1, 2)
        print("")
        if hero_attack == 1:
          print(player.melee_attack(enemy_list[2]))
        elif hero_attack == 2:
          print(player.ranged_attack(enemy_list[2]))
        
        if enemy_list[2].hp == 0:
          print(f"{enemy_list[2].name} has fallen.")
          enemy_list.pop(2)
        else:
          print(enemy_list[2].melee_attack(player))

      # End loop if player is defeated
      if player.hp == 0:
        print("")
        print(f"{player.name} has fallen.\nGame Over!")
        break

    if len(enemy_list) == 0:
      print("")
      print("Congrats! You defeated all three monsters!")
      print("Come back again, we will have more for you to slay!")

  # Expert Enemies
  elif difficulty == 2:
    exp_enemies = ExpertFactory()
    enemy_list = [exp_enemies.create_random_enemy(), exp_enemies.create_random_enemy(), exp_enemies.create_random_enemy()]

    # Continue battling until player defeats all enemies
    while len(enemy_list) != 0:
      print("")
      print("Choose an enemy to attack.")
      if len(enemy_list) == 3:
        print(f"1. {enemy_list[0]}")
        print(f"2. {enemy_list[1]}")
        print(f"3. {enemy_list[2]}")
      elif len(enemy_list) == 2:
        print(f"1. {enemy_list[0]}")
        print(f"2. {enemy_list[1]}")
      elif len(enemy_list) == 1:
        print(f"1. {enemy_list[0]}")
      who_to_attack = check_input.get_int_range("", 1, len(enemy_list))
  
      print("")
      if who_to_attack == 1:
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        hero_attack = check_input.get_int_range("", 1, 2)
        print("")
        if hero_attack == 1:
          print(player.melee_attack(enemy_list[0]))
        elif hero_attack == 2:
          print(player.ranged_attack(enemy_list[0]))
  
        if enemy_list[0].hp == 0:
          print(f"{enemy_list[0].name} has fallen.")
          enemy_list.pop(0)
        else:
          print(enemy_list[0].melee_attack(player))
      elif who_to_attack == 2:
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        hero_attack = check_input.get_int_range("", 1, 2)
        print("")
        if hero_attack == 1:
          print(player.melee_attack(enemy_list[1]))
        elif hero_attack == 2:
          print(player.ranged_attack(enemy_list[1]))
        
        if enemy_list[1].hp == 0:
          print(f"{enemy_list[1].name} has fallen.")
          enemy_list.pop(1)
        else:
          print(enemy_list[0].melee_attack(player))
      elif who_to_attack == 3:
        print(player)
        print("1. Sword Attack")
        print("2. Arrow Attack")
        hero_attack = check_input.get_int_range("", 1, 2)
        print("")
        if hero_attack == 1:
          print(player.melee_attack(enemy_list[2]))
        elif hero_attack == 2:
          print(player.ranged_attack(enemy_list[2]))
        
        if enemy_list[2].hp == 0:
          print(f"{enemy_list[2].name} has fallen.")
          enemy_list.pop(2)
        else:
          print(enemy_list[2].melee_attack(player))

      # End loop if player is defeated
      if player.hp == 0:
        print("")
        print(f"{player.name} has fallen.\nGame Over!")
        break

    if len(enemy_list) == 0:
      print("")
      print("Congrats! You defeated all three monsters!")
      print("Come back again, we will have more for you to slay!")


main()