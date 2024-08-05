from lib import cboslib
from lib.cboslib import version
import time
import requests
import colorama
import sys
import random
import pwinput
import runpy

cboslib.settitle("C-Bos")

cboslib.cprint("Booting cbos the crappy os...")
time.sleep(0.5)
cboslib.cprint("Checking for updates...")
cboslib.cprint(cboslib.versioncheck(version))
time.sleep(0.3)
cboslib.cprint("Done!")
time.sleep(0.3)
cboslib.cprint("Welcome to cbos! Type \"help\" for a list of commands!")
time.sleep(0.3)
adminyay = input(cboslib.randomstringcolor("Are you an admin? [Y/N]: ")).lower()

if(adminyay == "y"):
    admincode = pwinput.pwinput(prompt=cboslib.randomstringcolor("Put in the admin code: "))
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
        cboslib.cprint("6: Credits (Shows credits and some other stuff)")
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
        time.sleep(0.1)
        cboslib.cprint("12: Hello (says hi to you)")
        time.sleep(0.1)
        cboslib.cprint("13: Magic eight ball (let cbos decide your fate)")
        time.sleep(0.1)
        cboslib.cprint("14: Gui (An optional gui for cbos. Won't have all cbos features.)")

    elif(lowercmd == "base64 encode"):
        bumhole = cboslib.base64encode(input("String: "))
        print(bumhole)
        print("")
        time.sleep(1)
        cboslib.cprint("Btw if you want check out my base64 tool made in kotlin")
        cboslib.cprint("https://github.com/Thepuppetqueen57/Basket")

    elif(lowercmd == "base64 decode"):
        bum = cboslib.base64decode(input("Encoded string: "))
        print(bum)
        print("")
        time.sleep(1)
        cboslib.cprint("Btw if you want check out my base64 tool made in kotlin")
        cboslib.cprint("https://github.com/Thepuppetqueen57/Basket")

    elif(lowercmd == "check version"):
        cboslib.cprint(cboslib.versioncheck(version))

    elif(lowercmd == "credits"):
        print("Puppet: https://thepuppet57.alwaysdata.net")
        print("Dexter (theuntrueone): Dizzy5g on discord")
        print("Cj: http://butteredtoast.141412.xyz")
        print("C-Bos legacy: https://github.com/Thepuppetqueen57/C-Bos-Legacy")

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
            score = 0

            while gonnabeatyou != 10:
                score += 1
                gonnabeatyou = random.randint(1, 10)
                cboslib.cprint(f"You score is: {score}")
                time.sleep(0.05)
            highscore = cboslib.gethighscore()
            if(score > highscore):
                cboslib.updatehighscore(score)
        elif(kys == "high score"):
            highscore = cboslib.gethighscore()
            print(f"Your high score is {highscore}!")
        elif(kys == "help"):
            cboslib.cprint("The cbos luck game is a game where it generates a random number from 1 to 10")
            cboslib.cprint("It repeats this until the number is 10")
            cboslib.cprint("Every time it repeats your score goes up")
            cboslib.cprint("Try to get the highest score!")
            time.sleep(1)
            cboslib.cprint("Now here is a list of commands. There is only 1 rn.")
            time.sleep(0.3)
            cboslib.cprint("1: Play (plays the game)")
            time.sleep(0.1)
            cboslib.cprint("2: High score (Shows you your high score)")

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

    elif(lowercmd == "hello"):
        cboslib.cprintnnl("h")
        time.sleep(0.1)
        cboslib.cprintnnl("e")
        time.sleep(0.1)
        cboslib.cprintnnl("l")
        time.sleep(0.1)
        cboslib.cprintnnl("l")
        time.sleep(0.1)
        cboslib.cprintnnl("o")
        time.sleep(0.1)
        print("")

    elif(lowercmd == "magic eight ball"):
        question = input("Whats your question bro: ")
        print("Lemme think bro")
        time.sleep(1)
        print(cboslib.magicball())

    elif(lowercmd == "gui"):
        cboslib.cprint("Gui opened!")
        runpy.run_path("lib/gui.py")
        cboslib.cprint("Gui closed!")

    


    elif(isadmin):
        # The home of admin commands.
        if(lowercmd == "admin help"):
            print("there are currently no admin commands because I have no ideas for any at the moment")



        else:
            dumberror = cboslib.getdumberror()

            if(dumberror == True):
                print(f"{cmd} is stupid! try again!")
            else:
                print(f"{cmd} is an invalid command. Please try again!")


    
    else:
        dumberror = cboslib.getdumberror()

        if(dumberror == True):
            print(f"{cmd} is stupid! try again!")
        else:
            print(f"{cmd} is an invalid command. Please try again!")