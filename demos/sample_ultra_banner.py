# Ultra Rosé as an example
from banner import Banner
from account import Account
from colorama import Fore # good for making units look prettier
from get_dbl_chars import find_by_id # ID lookup function
import os

b = Banner("ULTRA RISING - RADIANT ROSÉ", "DBL57-01U", "", ["DBL41-02S", "DBL33-02S", "DBL24-01S", "DBL18-05S"], []) # 1 = name, 2 = main unit (rosé), 3 = one percent sp (left blank as there is not one), 4 = featured lfs, 5 = featured sps (2 but not in code yet, so left blank for now)
ac = Account("abcdefghij") # example ID used will open account with that ID

while True:
  print(b.name)
  print("Summon Step: " + str(b.step)) # free steps exist! if the step = 4, then you won't be charged! same for LF banners on step 6
  print("CC: " + str(ac.cc)) # print the amount of CC left
  sum = b.summon(ac) # the account has to be passed in order to check cc and add z power acquired from the summon
  if sum == []: # if there is not enough CC left, the summon will return an empty list
    break
  for _ in sum: # for unit in the multi
    _unit = find_by_id(_)
    if _.endswith("U"): # if the ID ends in U, it is an ultra, this will run when the ultra is acquired
        print(Fore.LIGHTBLUE_EX + "ULTRA " + _unit["name"] + Fore.RESET)
    elif _unit["lf"] == True: # if the unit has the LF tag, it will print it as LEGENDS LIMITED
        print(Fore.YELLOW + "LEGENDS LIMITED " + _unit["name"] + Fore.RESET)
    elif _unit["ID"].endswith("S"): # if the unit is a sparking, it will print it in yellow
        print(Fore.LIGHTYELLOW_EX + _unit["name"] + Fore.RESET)
    elif _unit["ID"].endswith("E"): # if the unit is an extreme, it will print it in purple
        print(Fore.MAGENTA + _unit["name"] + Fore.RESET)
    elif _unit["ID"].endswith("H"): # if the unit is a hero, it will print it in blue
        print(Fore.LIGHTCYAN_EX + _unit["name"] + Fore.RESET)
    else:
        print(_unit["name"]) # this block of code should never run, but it's there incase
    print("\n\n")
    os.system("pause") # just to stop infinite summoning, remove this if you just want the z power
