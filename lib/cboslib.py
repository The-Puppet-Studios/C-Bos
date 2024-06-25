import time
import requests
import colorama
import random
import ctypes
import sys
import os
import base64

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def randomcolor():
    color_choices = [
        colorama.Fore.RED,
        colorama.Fore.GREEN,
        colorama.Fore.YELLOW,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA,
        colorama.Fore.CYAN,
        colorama.Fore.LIGHTBLUE_EX,
        colorama.Fore.LIGHTCYAN_EX,
        colorama.Fore.LIGHTGREEN_EX,
        colorama.Fore.LIGHTMAGENTA_EX,
        colorama.Fore.LIGHTRED_EX,
        colorama.Fore.LIGHTYELLOW_EX
    ]
    return random.choice(color_choices)

def randomstringcolor(string):
    return randomcolor() + string + colorama.Fore.RESET

def cprint(string):
    print(randomstringcolor(string))

def versioncheck(version):
    url = "https://thepuppet57.141412.xyz/tps/cbos/backend/versioncheck.php"
    
    response = requests.get(url)
    latestversion = float(response.text)

    if(latestversion > version):
        cprint("Update available!")
    elif(latestversion < version):
        cprint("This is a beta!")
    else:
        cprint("No updates available!")

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
    url = 'https://thepuppet57.141412.xyz/tps/cbos/backend/adminauth.php'
    data = {
        'password': code
    }

    response = requests.post(url, data=data)


    if(response.status_code == 200):
        if(response.text == "yay"):
            return True
        else:
            return False
    else:
        return "There was an error. Status code:", response.status_code
    
def getservertext():
    url = "https://thepuppet57.141412.xyz/tps/cbos/backend/getservertext.php"

    response = requests.get(url)

    if(response.status_code == 200):
        print(response.text)
    else:
        print("There was an error. Status code:", response.status_code)

def editservertext(text):
    url = "https://thepuppet57.141412.xyz/tps/cbos/backend/editservertext.php"
    data = {
        "text": text
    }

    response = requests.post(url, data=data)

    if(response.status_code == 200):
        if(response.text == "The file has been updated successfully."):
            print("Text updated sccessfully!")
        else:
            print("Unknown error when editing text")
    else:
        print("There was an error. Status code:", response.status_code)

def randomghoststory():
    choices = [
        "cboscpp",
        "luckgameleaderboards",
        "xytriza"
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