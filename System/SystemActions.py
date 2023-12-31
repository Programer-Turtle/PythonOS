import time
import os
import System.errormanager as errormanager

def ClearScreen():
    os.system("cls")

def ShowArt(FileName):
    try:
        with open(os.path.join('System', "StyleData", FileName), "r") as LoadedArt:
            print(LoadedArt.read())
    except:
        errormanager.error("system", "Art file doesn't exist or is unreadable.")

def ShutDown():
    ClearScreen()
    ShowArt("ShutDownScreen.txt")
    time.sleep(3)
    exit()
