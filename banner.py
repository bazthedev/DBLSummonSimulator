import json
from get_dbl_chars import get_char_id, get_char_name, sort_event, sort_extreme, sort_hero, sort_sparking, sort_ultra, find_by_id, InvalidUnitError, sort_lf, sort_unfeatured, sort_not_event
import random
from account import Account
import os

if not os.path.exists(".\\banners.json"):
    with open("banners.json", "w") as f:
        json.dump({}, f, indent=4)

class Banner:

    def __init__(self, name : str, main: str, one_percent_sp : str, featured_lfs : list, featured_sp : list):
        self.name = name
        self.main = main
        with open("characters.json", "r") as f:
            chars = json.load(f)
        self.all_characters = chars
        all_lfs = sort_lf(self.all_characters)
        self.unfeatured_sp = sort_not_event(sort_unfeatured(sort_sparking(self.all_characters)))
        self.extreme = sort_extreme(self.all_characters)
        self.hero = sort_hero(self.all_characters)
        if self.main.endswith("U"):
            l = 4
            self.prices = [1000, 1000, 1000, 0]
            if featured_lfs != []:
                _provided_lfs = True
            else:
                _provided_lfs = False
        else:
            l = 8
            self.featured_sp = featured_sp
            i = 0
            for sp in self.unfeatured_sp:
                if sp in self.featured_sp:
                    self.unfeatured_sp.pop(i)
                i += 1
            self.prices = [300, 500, 700, 1000, 1000, 0]
            self.one_percent_sp = one_percent_sp
            if featured_lfs != []:
                _provided_lfs = True
            else:
                _provided_lfs = False
            if not self.validate_one_percent():
                raise InvalidUnitError("Your one percent sparking does not exist")
        self.step = 1
        while True:
            if _provided_lfs:
                self.featured_lfs = featured_lfs
                break
            _cont = False
            self.featured_lfs = []
            for i in range(l):
                if len(self.featured_lfs) == l:
                    _cont = False
                    break
                lf = random.choice(all_lfs)
                if lf["ID"] == self.main or lf["ID"] in self.featured_lfs:
                    _cont = True
                    continue
                self.featured_lfs.append(lf["ID"])
            if not _cont:
                break


        if not self.validate_main():
            raise InvalidUnitError("Your main featured unit does not exist")
        if not self.validate_featured():
            raise InvalidUnitError("One or more provided units are invalid")
        if not self.validate_lf():
            raise InvalidUnitError("One or more characters provided are not Legends Limited or do not exist")

    def validate_main(self):
        if find_by_id(self.main) != False:
            return True
        else:
            return False
        
    def validate_featured(self):
        valid = True
        if self.main.endswith("U"):
            return True
        if self.featured_sp == []:
            return True
        for _ in self.featured_sp:
            if find_by_id(_) == False:
                valid = False
        return valid
        
    def validate_one_percent(self):
        valid = True
        if find_by_id(self.one_percent_sp) == False:
            valid = False
        return valid
    
    def validate_lf(self):
        valid = True
        for lf in self.featured_lfs:
            _ = find_by_id(lf)
            if _ == False:
                valid = False
            if _["lf"] != True:
                valid = False
        return valid
    
    def get_lfs(self):
        lfs = []
        for _ in self.featured_lfs:
            lf = find_by_id(_)
            lfs.append(lf["name"])
        return lfs
    
    def summon(self, usr : Account):
        unit = None
        multi = []
        if self.main.endswith("U"):
            if self.step != 4:
                if usr.remove_cc(1000) == False:
                    print("Not enough CC")
                    return []
            for _ in range(1, 11):
                if self.step != 2:
                    if _ != 10:
                        pull = random.randint(0, 20000)
                        if pull <= 7:
                            unit = self.main
                            usr.add_z_power(unit, 2000)
                        elif pull > 7 and pull <= 407:
                            unit = random.choice(self.featured_lfs)
                            usr.add_z_power(unit, 600)
                        elif pull > 407 and pull <= 2007:
                            unit = random.choice(self.unfeatured_sp)["ID"]
                            usr.add_z_power(unit, 600)
                        elif pull > 1607 and pull <= 9007:
                            unit = random.choice(self.extreme)["ID"]
                            usr.add_z_power(unit, 250)
                        else:
                            unit = random.choice(self.hero)["ID"]
                            usr.add_z_power(unit, 100)
                    else:
                        pull = random.randint(0, 20000)
                        if pull <= 7:
                            unit = self.main
                            usr.add_z_power(unit, 2000)
                        elif pull > 407 and pull <= 2007:
                            unit = random.choice(self.featured_lfs)
                            usr.add_z_power(unit, 600)
                        else:
                            unit = random.choice(self.unfeatured_sp)["ID"]
                            usr.add_z_power(unit, 600)
                    multi.append(unit)
                else:
                    if _ != 10:
                        pull = random.randint(0, 20000)
                        if pull <= 14:
                            unit = self.main
                            usr.add_z_power(unit, 2000)
                        elif pull > 14 and pull <= 414:
                            unit = random.choice(self.featured_lfs)
                            usr.add_z_power(unit, 600)
                        elif pull > 414 and pull <= 2014:
                            unit = random.choice(self.unfeatured_sp)["ID"]
                            usr.add_z_power(unit, 600)
                        elif pull > 1614 and pull <= 9014:
                            unit = random.choice(self.extreme)["ID"]
                            usr.add_z_power(unit, 250)
                        else:
                            unit = random.choice(self.hero)["ID"]
                            usr.add_z_power(unit, 100)
                    else:
                        pull = random.randint(0, 20000)
                        if pull <= 14:
                            unit = self.main
                            usr.add_z_power(unit, 2000)
                        elif pull > 414 and pull <= 2014:
                            unit = random.choice(self.featured_lfs)
                            usr.add_z_power(unit, 600)
                        else:
                            unit = random.choice(self.unfeatured_sp)["ID"]
                            usr.add_z_power(unit, 600)
                    multi.append(unit)
            if self.step != 4:
                self.step += 1
            else:
                self.step = 1
        else:
            if self.step != 6:
                if usr.remove_cc(self.prices[(self.step - 1)]) == False:
                    print("Not enough CC")
                    return []
            print(str(self.prices[(self.step - 1)]))
            if self.step != 6:
                for i in range(0, (int(self.prices[(self.step - 1)] / 100))):
                    pull = random.randint(0, 10000)
                    if pull <= 50:
                        unit = self.main
                        usr.add_z_power(unit, 1200)
                    elif pull > 50 and pull <= 250:
                        unit = random.choice(self.featured_lfs)
                        usr.add_z_power(unit, 1200)
                    elif pull > 250 and pull <= 350:
                        unit = self.one_percent_sp
                        usr.add_z_power(unit, 1200)
                    elif pull > 350 and pull <= 2750:
                        unit = random.choice(self.unfeatured_sp)["ID"]
                        usr.add_z_power(unit, 1200)
                    elif pull > 2750 and pull <= 6250:
                        unit = random.choice(self.extreme)["ID"]
                        usr.add_z_power(unit, 500)
                    else:
                        unit = random.choice(self.hero)["ID"]
                        usr.add_z_power(unit, 200)
                    multi.append(unit)
            else:
                for i in range(0, 10):
                    pull = random.randint(0, 10000)
                    if pull <= 50:
                        unit = self.main
                        usr.add_z_power(unit, 1200)
                    elif pull > 50 and pull <= 250:
                        unit = random.choice(self.featured_lfs)
                        usr.add_z_power(unit, 1200)
                    elif pull > 250 and pull <= 350:
                        unit = self.one_percent_sp
                        usr.add_z_power(unit, 1200)
                    elif pull > 350 and pull <= 2750:
                        unit = random.choice(self.unfeatured_sp)["ID"]
                        usr.add_z_power(unit, 1200)
                    elif pull > 2750 and pull <= 6250:
                        unit = random.choice(self.extreme)["ID"]
                        usr.add_z_power(unit, 500)
                    else:
                        unit = random.choice(self.hero)["ID"]
                        usr.add_z_power(unit, 200)
                    multi.append(unit)
            if self.step != 6:
                self.step += 1
            else:
                self.step = 2
        return multi
    
    def save_banner(self):
        with open("banners.json", "r") as f:
            banners = json.load(f)
            banners[self.name] = {
                "name" : self.name,
                "main": self.main,
                "lfs": self.featured_lfs,
                "sps" : self.featured_sp,
                "step" : self.step,
                "price" : self.prices
            }
        with open("banners.json", "w") as f:
            json.dump(banners, f, indent=4)
