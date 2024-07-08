import json
import string
import random
import os

if not os.path.exists(".\\accounts.json"):
    with open("accounts.json", "w") as f:
        json.dump({}, f, indent=4)

class Account():

    def __init__(self, id = ""):
        with open("accounts.json", "r") as f:
            accounts = json.load(f)
            if id in accounts:
                self.id = id
                self.name = accounts[self.id]["name"]
                self.units = accounts[self.id]["units"]
                self.cc = accounts[self.id]["cc"]
            elif id == "":
                with open("characters.json", "r") as c:
                    chars = json.load(c)
                    self.id = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
                    self.name = input("Choose a name: ")
                    self.units = {}
                    for _c in chars["characters"]:
                        self.units[_c["ID"]] = 0
                    self.cc = 0
                accounts[self.id] = {
                    "name" : self.name,
                    "units" : self.units,
                    "cc" : self.cc
                }
                print(self.id)
        with open("accounts.json", "w") as f:
            json.dump(accounts, f, indent=4)
        self.accounts = accounts
        
    def remove_cc(self, cc : int):
        if cc > self.cc or cc <= 0:
            return False
        self.accounts[self.id]["cc"] -= cc
        self.cc -= cc
        with open("accounts.json", "w") as f:
            json.dump(self.accounts, f, indent=4)
        return True
    
    def give_cc(self, cc : int):
        if cc <= 0:
            return False
        self.accounts[self.id]["cc"] += cc
        self.cc += cc
        with open("accounts.json", "w") as f:
            json.dump(self.accounts, f, indent=4)
        return True
    
    def add_z_power(self, unit : str, z_pwr : int):
        self.accounts[self.id]["units"][unit] += z_pwr
        self.units[unit] += z_pwr
        with open("accounts.json", "w") as f:
            json.dump(self.accounts, f, indent=4)

    def reset_chars(self):
        for char in self.accounts[self.id]["units"]:
            self.accounts[self.id]["units"][char] = 0
        with open("accounts.json", "w") as f:
            json.dump(self.accounts, f, indent=4)
        self.units = self.accounts[self.id]["units"]
