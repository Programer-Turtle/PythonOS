import System.errormanager as errormanager
import platform
import time
import os

CurrentOS = platform.system()

def ClearScreen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def ShowArt(FileName):
    try:
        with open(os.path.join('System', "StyleData", FileName), "r") as LoadedArt:
            print(LoadedArt.read())
    except:
        errormanager.error("system", "Art file doesn't exist or is unreadable.")

def RestoreColor():
    if CurrentOS == "Windows":
        with open(os.path.join("System", "StyleData", "TextColor.txt"), "r") as ColorCode:
            os.system(f"color {ColorCode.read()}")
    else:
        ClearScreen()

def ShutDown():
    ClearScreen()
    ShowArt("ShutDownScreen.txt")
    time.sleep(3)
    exit()