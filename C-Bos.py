from lib import cboslib
import time
import requests
import colorama
import ctypes
import sys

cboslib.settitle("C-Bos")

cboslib.cprint("Booting cbos the crappy os...")
time.sleep(0.5)
version = 2.1
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

    elif(lowercmd == "base64 encode"):
        bumhole = cboslib.base64encode(input("String: "))
        print(bumhole)

    elif(lowercmd == "base64 decode"):
        bum = cboslib.base64decode(input("Encoded string: "))
        print(bum)

    elif(lowercmd == "check version"):
        cboslib.versioncheck(version)

    

    elif(isadmin):
        # The home of admin commands.
        if(lowercmd == "admin real"):
            print("yay")
    
    elif(lowercmd == "SubToPuppet"):
        print("https://www.youtube.com/@thepuppetqueen57")
        elif(lowercmd == "SubToCJ"):
        print("butteredtoast.141412.xyz")
    else:
        print(f"{cmd} is stupid! try again!")