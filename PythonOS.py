import os
import time
#Boot
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.system("cls")

try:
    with open(os.path.join("System", "StyleData", "TextColor.txt"), "r") as ColorCode:
        os.system(f"color {ColorCode.read()}")
except:
    print("SettingDefaultColor...")
    with open(os.path.join("System", "StyleData", "TextColor.txt"), "w") as ColorCode:
        ColorCode.write("0a")
        os.system("color 0a")
        os.system("cls")

try:
    import System.Fixer as Fixer
except:
    print("Fixer is missing.")
    print("1.ShutDown")
    print("2.Attempt Boot")
    while True:
        choice = input("Repair>")
        if choice == "1":
            print("ShuttingDown...")
            time.sleep(3)
            exit()
        elif choice == "2":
            print("AtemptingBoot...")
            time.sleep(3)
            break
try:
    import System.errormanager as ErrorManager

except:
    print("The system error detection system is missing or corupted. Please reinstall.")
    print("1. ShutDown")
    print("2. Install Error Detection System Using Backup")
    while True:
        choice = input("Repair>")
        if choice == "1":
            print("ShuttingDown...")
            time.sleep(3)
            exit()
        elif choice == "2":
            Fixer.InstallErrorManagerBackup()
            print("Shutdown Rquired")
            print("Reopen Python OS after shutdown.")
            time.sleep(1)
            print("ShuttingDown...")
            time.sleep(3)
            exit()

try:
    from System.SystemActions import *

except:
    print("SystemActions is missing or corrupted. Please reinstall.")
    print("1. ShutDown")
    print("2. Install SystemActions Using Backup")
    while True:
        choice = input("Repair>")
        if choice == "1":
            print("ShuttingDown...")
            time.sleep(3)
            exit()
        elif choice == "2":
            Fixer.InstallSystemActionsBackup()
            print("Shutdown Rquired")
            print("Reopen Python OS after shutdown.")
            time.sleep(1)
            print("ShuttingDown...")
            time.sleep(3)
            exit()


try:
    import System.Programs.ProgramManager as ProgramManager
except:
    print("Program Manager is missing or corrupted. Please reinstall.")
    print("1. ShutDown")
    print("2. Install Program Manager Using Backup")
    while True:
        choice = input("Repair>")
        if choice == "1":
            print("ShuttingDown...")
            time.sleep(3)
            exit()
        elif choice == "2":
            Fixer.InstallProgramManagerBackup()
            print("Shutdown Rquired")
            print("Reopen Python OS after shutdown.")
            time.sleep(1)
            print("ShuttingDown...")
            time.sleep(3)
            exit()


print("Booting...")
os.system("cls")
try :
    with open(os.path.join("System", "StyleData", "StartUpScreenArt.txt"), "r") as BootArt:
        print(BootArt.read())
        time.sleep(3)
    
except:
    ErrorManager.error("system", "BootArt is missing would you like to still attempt boot?")
    print("1. ShutDown")
    print("2. Attempt Boot (Other Systems may be broken aswell)")
    while True:
        choice = input("Repair>")
        if choice == "1":
            print("ShuttingDown...")
            time.sleep(3)
            exit()
        elif choice == "2":
            Fixer.InstallErrorManagerBackup()
            print("Atempting Boot...")
            time.sleep(3)
            break

def About():
    ClearScreen()
    ShowArt("Logo.txt")
    print("Hello welcome to Python OS. This program has some scripts from python like the ascii art and the preinstalled adventure game. This program has the capability to run python code. In the future we plan to add file handling. If you need help type '?' or 'help'.")
    print("Feel free to modify Python OS code if you want to make your own.")

def SetColor(color):
    try:
        os.system(f"color {color}")
        with open(os.path.join("System", "StyleData", "TextColor.txt"), "w") as TextColorFile:
            TextColorFile.write(color)
        return
    except:
        errormanager.error("user", "Invalid Color Code")

def RunProgramManager():
    ClearScreen()
    ProgramManager.ProgramManagerMain()
    About()

def CheckIfProgramName(command):
    programList = ProgramManager.GetProgramList()
    if command in programList:
        ProgramManager.RunProgram(command)
        return True
    else:
        return False

def Help():
    try:
        with open(os.path.join("System", "Help.txt"), "r") as HelpFile:
            print(HelpFile.read())
    except:
        errormanager.error("system", "Help data is missing try to reinstall Python OS.")

About()
while True:
    try:
        RawCommand = input("PythonOS>")
        Command = RawCommand.lower()
        if Command == "cls" or Command == "clear":
            ClearScreen()
        elif Command == "shutdown":
            ShutDown()
        elif Command == "about":
            About()
        elif Command == "programmanager":
            RunProgramManager()
        elif Command[0:5] == "color":
            SetColor(Command[6:])
        elif Command == "help" or Command == "?":
            Help()
        else:
            if CheckIfProgramName(RawCommand):
                
                print("Program has stopped.")
            else:
                ErrorManager.error("user", f"{RawCommand} is not a valid command or program name, or other error has occured.")
    
    except Exception as e:
        ErrorManager.error("system", e)