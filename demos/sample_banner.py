# Super Baby 2 (DBL69-01S) Banner as an example:
from banner import Banner
from account import Account
from colorama import Fore # good for making units look prettier
from get_dbl_chars import find_by_id # ID lookup function
import os

super_baby_banner = Banner("VENGEFUL NEOMACHINE MUTANT", "DBL69-01S", "DBL69-02S", ["DBL61-03S", "DBL60-02S", "DBL53-01S", "DBL44-01S", "DBL35-08S", "DBL35-01S"], ["DBL59-04S", "DBL54-04S", "DBL53-03S"]) # 1 = banner name, 2 = main featured unit, 3 = one percent sp, 4 = list of featured lfs, 5 = list of featured sp
ac = Account("") # leaving this as "" will make a new account, but if you put your ID in there, it will load your characters and CC, e.g. if ID was "abcdefghij", then it would load that account

while True:
  print(super_baby_banner.name)
  print("Summon Step: " + str(super_baby_banner.step))
  print("CC: " + str(ac.cc))
  sum = super_baby_banner.summon(ac) # the account has to be passed in order to check cc and add z power acquired from the summon
  if sum == []: # if there is not enough CC left, the summon will return an empty list
    break
  for _ in sum: # for unit in the multi
    _unit = find_by_id(_)
    if _.endswith("U"): # if the ID ends in U, it is an ultra, however this will not run as this is an LF banner
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
        print(a["name"]) # this block of code should never run, but it's there incase
    print("\n\n")
    os.system("pause") # just to stop infinite summoning, remove this if you just want the z power
