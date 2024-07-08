import json
import requests
from bs4 import BeautifulSoup as bs
import os
import time

def get_ld_json(html):
    soup = bs(str(html), "html.parser")
    return json.loads("".join(soup.find("script", {"type": "application/ld+json"}).contents))

def get_char_name(_json):
    return _json["headline"].split(" Character Details")[0]

if not os.path.exists(".\\characters.json"):
    with open("characters.json", "w") as f:
        ch = {}
        ch["no_characters"] = 0
        ch["no_new_characters"] = 618
        ch["characters"] = []
        json.dump(ch, f, indent=4)


class InvalidUnitError(Exception):
    pass

def sort_not_event(_json):
    sorted = []
    for character_ in _json:
        if "EVT" not in character_["name"]:
            sorted.append(character_)
    return sorted

def sort_event(_json):
    sorted = []
    for character in _json["characters"]:
        if "EVT" in character:
            sorted.append(character)
    return sorted

def sort_ultra(_json):
    sorted = []
    for ch in _json["characters"]:
        if ch["ID"].endswith("U"):
            sorted.append(ch)
    return sorted

def sort_sparking(_json):
    sorted = []
    for ch in _json["characters"]:
        if ch["ID"].endswith("S"):
            sorted.append(ch)
    return sorted

def sort_extreme(_json):
    sorted = []
    for ch in _json["characters"]:
        if ch["ID"].endswith("E"):
            sorted.append(ch)
    return sorted

def sort_hero(_json):
    sorted = []
    for ch in _json["characters"]:
        if ch["ID"].endswith("H"):
            sorted.append(ch)
    return sorted

def sort_lf(_json):
    sorted = []
    for ch in _json["characters"]:
        if ch["lf"] == True:
            sorted.append(ch)
    return sorted

def fix_amp():
    with open("characters.json", "r") as f:
        chars = json.load(f)
        i = 0
        for _ in chars["characters"]:
            if "amp;" in _["name"]:
                fixed_name = chars["characters"][i]["name"].replace("amp;", "")
                fixed_desc = chars["characters"][i]["description"].replace("amp;", "")
                fixed_head = chars["characters"][i]["headline"].replace("amp;", "")
                chars["characters"][i]["name"] = fixed_name
                chars["characters"][i]["description"] = fixed_desc
                chars["characters"][i]["headline"] = fixed_head
            i += 1
    with open("characters.json", "w") as f:
        json.dump(chars, f, indent=4)

def check_new_char():
    with open("characters.json", "r") as f:
        nc = False
        chars = json.load(f)
        _character = requests.get(f"https://legends.dbz.space/characters/{(chars["no_new_characters"] + 1)}")
        x = get_ld_json(_character.text)
        x["name"] = get_char_name(x)
        if x["name"] != "":
            download_character((chars["no_new_characters"] + 1))
            nc = True
            print(f"Found new character {x["name"]}")
    if nc:
        check_new_char()

def get_char_id(_json, char_no):
    for _ in _json["characters"]:
        if _["number"] == char_no:
            id = _["name"][-10:-1]
            print(id)
    return id

def set_id():
    with open("characters.json", "r") as f:
        chars = json.load(f)
        i = 0
        for _ in chars["characters"]:
            if "EVT" not in _["name"]:
                chars["characters"][i]["ID"] = _["name"][-10:-1]
            else:
                chars["characters"][i]["ID"] = _["name"][-12:-1]
            i += 1
    with open("characters.json", "w") as f:
        json.dump(chars, f, indent=4)

def find_by_id(id):
    with open("characters.json", "r") as f:
        chars = json.load(f)
        for _ in chars["characters"]:
            if _["ID"] == id:
                return _
        return False

def download_character(char_no : int):
    with open("characters.json", "r") as f:
        chars = json.load(f)
        _character = requests.get(f"https://legends.dbz.space/characters/{char_no}")
        x = get_ld_json(_character.text)
        x["name"] = get_char_name(x)
        if x["name"] == "":
            return
        x["number"] = char_no
        print(x["name"])
        chars["characters"].append(x)
    with open("characters.json", "w") as f:
        chars["no_characters"] = len(chars["characters"])
        chars["no_new_characters"] += 1
        json.dump(chars, f, indent=4)

def remove_blank():
    with open("characters.json", "r") as f:
        chars = json.load(f)
        i = 0
        for _ in chars["characters"]:
            if _["name"] == "":
                chars["characters"].pop(i)
            i += 1
    with open("characters.json", "w") as f:
        json.dump(chars, f, indent=4)

def find_exists():
    with open("characters.json", "r") as f:
            chars = json.load(f)
            exists = []
            for _ in chars["characters"]:
                exists.append(_["number"])
    return exists

def sort_unfeatured(_json):
    sorted = []
    for ch in _json:
        if ch["number"] > 502:
            continue
        if ch["ID"].endswith("U"):
            continue
        if ch["lf"] == True:
            continue
        sorted.append(ch)
    return sorted

def remove_useless():
    with open("characters.json", "r") as f:
        chars = json.load(f)
        i = 0
        for _ in chars["characters"]:
            try:
                del chars["characters"][i]["@context"]
                del chars["characters"][i]["@type"]
                del chars["characters"][i]["publisher"]
            except KeyError:
                pass
            i += 1
    with open("characters.json", "w") as f:
        json.dump(chars, f, indent=4)

def fix_rose(): # é
    with open("characters.json", "r") as f:
        chars = json.load(f)
        i = 0
        for _ in chars["characters"]:
            if "&eacute;" in _["name"]:
                fixed_name = chars["characters"][i]["name"].replace("&eacute;", "é")
                fixed_desc = chars["characters"][i]["description"].replace("&eacute;", "é")
                fixed_head = chars["characters"][i]["headline"].replace("&eacute;", "é")
                chars["characters"][i]["name"] = fixed_name
                chars["characters"][i]["description"] = fixed_desc
                chars["characters"][i]["headline"] = fixed_head
            i += 1
    with open("characters.json", "w") as f:
        json.dump(chars, f, indent=4)

def fix_chars():
    set_id()
    remove_blank()
    fix_amp()
    fix_rose()
    remove_useless()

def backup_chars():
    with open("characters.json", "r") as f:
        chars = json.load(f)
    with open("characters.json.bak", "w") as f:
        json.dump(chars, f, indent=4)

def import_backup():
    with open("characters.json.bak", "r") as f:
        chars = json.load(f)
    with open("characters.json", "w") as f:
        json.dump(chars, f, indent=4)

def find_characters():
    exists = find_exists()
    with open("characters.json", "r") as f:
        chars = json.load(f)
        if chars["no_new_characters"] == chars["no_characters"]:
            return
        for character in range(chars["no_new_characters"]):
            _ch = chars["no_new_characters"] - character
            if _ch in exists:
                continue
            _character = requests.get(f"https://legends.dbz.space/characters/{_ch}")
            if "blocked" in _character.text.lower():
                print("Blocked, retrying in 60 seconds")
                time.sleep(60)
                _character = requests.get(f"https://legends.dbz.space/characters/{_ch}")
            x = get_ld_json(_character.text)
            x["name"] = get_char_name(x)
            if x["name"] == "":
                continue
            x["number"] = _ch
            print(x["name"])
            if "legends-limited" in _character.text:
                x["lf"] = True
            else:
                x["lf"] = False
            chars["characters"].append(x)
            time.sleep(2)
            if (character % 10) == 0:
                with open("characters.json", "w") as f:
                    print("Saving downloaded characters...")
                    chars["no_characters"] = len(chars["characters"])
                    print("Saved")
                    json.dump(chars, f, indent=4)
    with open("characters.json", "w") as f:
        chars["no_characters"] = len(chars["characters"])
        json.dump(chars, f, indent=4)

if __name__ == "__main__": 
    backup_chars()
    find_characters()
    check_new_char()
    fix_chars()
