import time
import requests
import colorama
import random
import ctypes
import sys
import os
import base64
import json
from collections import namedtuple

# These are variables for links.
# Makes changing links faster for if links change for some reason.
versionchecklink = "https://thepuppet57.alwaysdata.net/tps/cbos/backend/versioncheck.php"
getservertextlink = "https://thepuppet57.alwaysdata.net/tps/cbos/backend/getservertext.php"
editservertextlink = "https://thepuppet57.alwaysdata.net/tps/cbos/backend/editservertext.php"
adminauthlink = "https://thepuppet57.alwaysdata.net/tps/cbos/backend/adminauth.php"

version = 3.00

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def randomcolor():
    color_choices = [
        colorama.Fore.RED,
        colorama.Fore.GREEN,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN,
        colorama.Fore.LIGHTBLUE_EX,
        colorama.Fore.LIGHTCYAN_EX,
        colorama.Fore.LIGHTGREEN_EX,
        colorama.Fore.LIGHTMAGENTA_EX,
        colorama.Fore.LIGHTRED_EX,
    ]
    return random.choice(color_choices)

def randomstringcolor(string):
    return randomcolor() + string + colorama.Fore.RESET

def cprint(string):
    print(randomstringcolor(string))


def versioncheck(version):
    try:
        data = {
            "edition": "normal"
        }

        response = requests.get(versionchecklink, params=data)
        latestversion = float(response.text)

        # Then this is basic logic really not hard to understand
        if(latestversion > version):
            return "Update available!"
        elif(latestversion < version):
            return "This is a beta!"
        else:
            return "No updates available!"
    except:
        return "Version check failed. Please check your internet connection."

def base64encode(string):
    encoded_bytes = base64.b64encode(string.encode("utf-8"))
    encoded_str = encoded_bytes.decode("utf-8")
    return encoded_str

def base64decode(encoded_str):
    decoded_bytes = base64.b64decode(encoded_str.encode("utf-8"))
    decoded_str = decoded_bytes.decode("utf-8")
    return decoded_str

def settitle(title):
    # ok so basically windows is special and has stuff in python that no other os has.
    # only found this issue recently cuz I tried running cbos on my arch linux vm
    if os.name == 'nt':  # nt means windows
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        # on unix-like systems, you can use the `tput` command to set terminal title
        print(f'\33]0;{title}\a', end='', flush=True)

def adminauth(code):
    data = {
        'password': code
    }

    response = requests.post(adminauthlink, data=data)


    if(response.status_code == 200):
        if(response.text == "yay"):
            return True
        else:
            return False
    else:
        return "There was an error. Status code:", response.status_code
    
def getservertext():
    response = requests.get(getservertextlink)

    if(response.status_code == 200):
        print(response.text)
    else:
        print("There was an error. Status code:", response.status_code)

def editservertext(text):
    url = editservertextlink
    data = {
        "text": text
    }

    response = requests.post(url, data=data)

    if(response.status_code == 200):
        if(response.text == "The file has been updated successfully."):
            print("Text updated sccessfully!")
        elif(response.text == "Script tag detected. The server text has not been edited."):
            print("Javascript detected. The server text has not been edited.")
        else:
            print("Unknown error when editing text")
    else:
        print("There was an error. Status code:", response.status_code)

def randomghoststory():
    choices = [
        "cboscpp",
        "luckgameleaderboards",
        "xytriza",
        "oldhelp"
    ]

    story = random.choice(choices)

    if(story == "cboscpp"):
        cprint("Once...")
        time.sleep(3)
        cprint("For a very short time...")
        time.sleep(3)
        cprint("There was a version of cbos written in c++ but...")
        time.sleep(3)
        cprint("Theres this thing called...")
        time.sleep(3)
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "CURL" + colorama.Style.RESET_ALL)
        time.sleep(3)
        cprint("It was a c++ library to interact with a server... But it brought PAIN AND SUFFERING")
        time.sleep(3)
        cprint("And thats the story of how cbos was rewritten in python instead of c++")

    elif(story == "luckgameleaderboards"):
        cprint("Once...")
        time.sleep(3)
        cprint("Puppet tried making leaderboards for the luck game...")
        time.sleep(3)
        cprint("This was never completed because...")
        time.sleep(3)
        cprint("Puppet slowly went insane trying to make it...")
        time.sleep(3)
        cprint("Then she snapped and deleted all the changes...")
        time.sleep(3)
        cprint("The code was never seen again...")
        time.sleep(3)
        cprint("And thats the story of how the luck game never got leaderboards")

    elif(story == "xytriza"):
        cprint("Once...")
        time.sleep(3)
        cprint("There was a second dev for cbos...")
        time.sleep(3)
        cprint("His name was...")
        time.sleep(3)
        cprint("Xytriza...")
        time.sleep(3)
        cprint("One day he deleted his github account...")
        time.sleep(3)
        cprint("Never to be seen again...")
        time.sleep(3)
        cprint("And thats the story of how xytriza died")

    elif(story == "oldhelp"):
        cprint("Once...")
        time.sleep(3)
        cprint("In the original cbos...")
        time.sleep(3)
        cprint("There was... The old help command...")
        time.sleep(3)
        cprint("The old help command had ZERO new lines...")
        time.sleep(3)
        cprint("Is was a disgusting mess...")
        time.sleep(3)
        cprint("Then it was replaced in cbos 1.1 never to be seen again...")
        time.sleep(3)
        cprint("And thats the story of how the help command isnt garbage anymore")

def updatehighscore(new_highscore):
    file_path = os.path.join('lib', 'stuff.json')

    with open(file_path, 'r') as file:
        data = json.load(file)

    data['luckgamedata']['highscore'] = new_highscore

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def gethighscore():
    file_path = os.path.join('lib', 'stuff.json')

    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as file:
        data = json.load(file)

    return data['luckgamedata']['highscore']

def getdumberror():
    json_path = os.path.join('lib', 'stuff.json')

    with open(json_path, 'r') as file:
        data = json.load(file)

    if data.get('options', {}).get('dumberror', False):
        return True
    else:
        return False
    
def printnnl(strulung):
    print(strulung, end="", flush=True)

def cprintnnl(poo):
    print(randomstringcolor(poo), end="", flush=True)

def magicball():
    outcomes = [
        "Nope",
        "Nuh uh",
        "Maybe idk",
        "I don't get paid enough for this",
        "Yea bro",
        "Your question is stupid so I won't answer",
        "This is so cool bro so like yeah",
        "yes yes"
    ]

    outcome = random.choice(outcomes)

    return outcome

def getversion(version):
    Result = namedtuple('Result', ['latestversion', 'version'])
    try:
        Error = "Version check failed. Please check your internet connection."

        data = {
            "edition": "normal"
        }

        response = requests.get(versionchecklink, params=data)
        latestversion = float(response.text)

        return Result(latestversion, version)

        
    except:
        return Result(Error, Error)