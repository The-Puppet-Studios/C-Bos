from lib import cboslib
import time
import requests
import colorama
import sys
import random

cboslib.settitle("C-Bos")

cboslib.cprint("Booting cbos the crappy os...")
time.sleep(0.5)
version = 2.12
cboslib.cprint("Checking for updates...")
cboslib.versioncheck(version)
time.sleep(0.3)
cboslib.cprint("Done!")
time.sleep(0.3)
cboslib.cprint("Welcome to cbos! Type \"help\" for a list of commands!")
time.sleep(0.3)
adminyay = input(cboslib.randomstringcolor("Are you an admin? [Y/N]: ")).lower()

if(adminyay == "y"):
    admincode = input(cboslib.randomstringcolor("Put in the admin code: "))
    cboslib.cprint("Authenticating...")
    isadmin = cboslib.adminauth(admincode)
    if(isadmin == True):
        cboslib.cprint("Admin code is correct!")
    else:
        cboslib.cprint("Admin code not correct.")
else:
    cboslib.cprint("Not an admin...")
    isadmin = False

time.sleep(0.3)

cmdloop = True
while cmdloop:
    cmd = input(colorama.Fore.GREEN + "> " + colorama.Fore.RESET)
    lowercmd = cmd.lower()

    if(lowercmd == "run test"):
        print("Its workin!")

    elif(lowercmd == "shut down" or lowercmd == "exit"):
        print("Shutting down...")
        time.sleep(0.5)
        sys.exit()

    elif(lowercmd == "help"):
        cboslib.cprint("1: Run test (it was in the original so I put it here idk)")
        time.sleep(0.1)
        cboslib.cprint("2: Exit (exits the program wowie)")
        time.sleep(0.1)
        cboslib.cprint("3: Base64 encode (encodes text)")
        time.sleep(0.1)
        cboslib.cprint("4: Base64 decode (decodes text)")
        time.sleep(0.1)
        cboslib.cprint("5: Check version (checks for updates)")
        time.sleep(0.1)
        cboslib.cprint("6: Credits (Shows credits)")
        time.sleep(0.1)
        cboslib.cprint("7: Get server text (Shows the text of a txt file on the server)")
        time.sleep(0.1)
        cboslib.cprint("8: Edit server text (Edits a txt on the server)")
        time.sleep(0.1)
        cboslib.cprint("9: Luck game (A little game about luck)")
        time.sleep(0.1)
        cboslib.cprint("10: Ghost story (Tells a random ghost story)")
        time.sleep(0.1)
        cboslib.cprint("11: How to add a command (Shows a guide on how to add a command)")

    elif(lowercmd == "base64 encode"):
        bumhole = cboslib.base64encode(input("String: "))
        print(bumhole)

    elif(lowercmd == "base64 decode"):
        bum = cboslib.base64decode(input("Encoded string: "))
        print(bum)

    elif(lowercmd == "check version"):
        cboslib.versioncheck(version)

    elif(lowercmd == "credits"):
        print("Puppet: https://thepuppet57.141412.xyz")
        print("Cj: http://butteredtoast.141412.xyz")

    elif(lowercmd == "get server text"):
        cboslib.getservertext()
    
    elif(lowercmd == "edit server text"):
        boobiehahahaha = input("New text: ")
        cboslib.editservertext(boobiehahahaha)

    elif(lowercmd == "luck game"):
        cboslib.cprint("Type help for what you can do")
        kys = input(cboslib.randomstringcolor("What do you want to do: ")).lower()
        if(kys == "play"):
            gonnabeatyou = 0
            nope = 0

            while gonnabeatyou != 10:
                nope += 1
                gonnabeatyou = random.randint(1, 10)
                cboslib.cprint(f"You score is: {nope}")
                time.sleep(0.05)
        elif(kys == "help"):
            cboslib.cprint("The cbos luck game is a game where it generates a random number from 1 to 10")
            cboslib.cprint("It repeats this until the number is 10")
            cboslib.cprint("Every time it repeats your score goes up")
            cboslib.cprint("Try to get the highest score!")
            time.sleep(1)
            cboslib.cprint("Now here is a list of commands. There is only 1 rn.")
            time.sleep(0.3)
            cboslib.cprint("1: Play (plays the game)")

    elif(lowercmd == "ghost story"):
        cboslib.randomghoststory()

    elif(lowercmd == "how to add a command"):
        cboslib.cprint("Open cbos.py with vs code")
        time.sleep(0.5)
        cboslib.cprint("And right below the bottom elif add another elif")
        time.sleep(0.5)
        cboslib.cprint("Example: elif(lowercmd == \"this is whatever you want the command to be\"): code to run")
        time.sleep(0.5)
        cboslib.cprint("You can probably figure out how to make a function in cboslib.py and if not tell me to add a guide for that")
        time.sleep(0.5)        
    


    elif(isadmin):
        # The home of admin commands.
        if(lowercmd == "admin real"):
            print("yay")


    
    else:
        print(f"{cmd} is stupid! try again!")