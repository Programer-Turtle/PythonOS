import os
import subprocess
import platform
import shutil
from .. import errormanager
from .. import SystemActions

currentOS = platform.system()

def GetProgramList():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    # Get all files in the folder
    directories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    if "__pycache__" in directories:
        directories.remove("__pycache__")
    
    return directories

#AutoPip
def GetPipList(file):
    Failed_List = []
    for line in file:
        try:
            if "None" in line:
                return "None"
            exec(f"import {line}")
        except:
            Failed_List.append(line)

    if Failed_List == []:
        return "None"
    return Failed_List

def InsatllModuels(InstallList):
    for moduel in InstallList:
        failedList = []
        print(f"Installing {moduel}")
        try:
            os.system(f"pip install {moduel}")
            print(f"AutoPip insalled {moduel} successfully")
        except:
            errormanager.error("system" , f"Failed to install {moduel}. Auto Pip file could be incorrectly setup.")
            failedList.append(moduel)
    return failedList


def AutoPip(ProgramPath):
    try:
        with open(os.path.join(ProgramPath, "install.PyOSPip")) as PipData:
            Install_List = GetPipList(PipData)
            if Install_List == "None":
                print("No Installs Needed")
                return
            if InsatllModuels(Install_List) == []:
                print("AutoPip installed all modules.")
                return
            else:
                errormanager.error("system", "Some installs failed program may not run.")
                return
        
                      
    except:
        print("No AutoPip Found")
        return

#Run programs
def RunProgram(program_Name):
    try:
       program_path = os.path.join("System", "Programs", program_Name)
       print("Running Auto Pip")
       AutoPip(program_path)
       SystemActions.RestoreColor()
       with open(os.path.join(program_path, "index.py"), "r"):
           print("Program index.py file found. Running Progam")
       subprocess.run(['python', os.path.join(program_path, "index.py")])
    except:
        errormanager.error("user", "File Not Found or does not contain 'index.py' file. Program May have also ended.")

def RunProgramUI():
    program_list = GetProgramList()

    print("Programs:")
    for count, folder in enumerate(program_list, start=1):
        print(f"{count}.{folder}")
    while True:
        print("What program would you like to run?")
        Progrm = input("Runner>")
        if Progrm.lower() == "exit":
            print("Exited...")
            return
        if Progrm in program_list:
            RunProgram(Progrm)
            print("Program has stopped.")
            return
        else:
            try:
                programIndex = int(Progrm)
                if program_list[programIndex - 1] != "" or program_list[programIndex - 1] != None:
                    RunProgram(program_list[programIndex - 1])
                    print("Program has stopped.")
                    return
            except:
                errormanager.error("user", "Program does not exist.")
#Install Programs
def MoveInstall(path):
    try:
        shutil.move(path, os.path.join("System", "Programs"))
        return True
    except:
        errormanager.error("user", "Program does not exist at this path or program already has the same name.")
        return False

def CopyInstall(path):
    try:
        directory_name = os.path.basename(path)
        shutil.copytree(path, os.path.join("System", "Programs", directory_name))
        return True
    except:
        errormanager.error("user", "Program does not exist at this path or program already has the same name.")
        return False

def InstallProgram(path, MoveOrCopy):
    if MoveOrCopy.lower() == "move":
        return MoveInstall(path)
    elif MoveOrCopy.lower() == "copy":
        return CopyInstall(path)
    else:
        errormanager.error("system", "Not valid install type. For developer.")

def InstallProgramUI():
    while True:
        print("What is the path of the program on your computer? IMPORTANT make sure the program's main file is named 'index.py' before installing. *Python OS does not support installing from the internet currently, so the program must already be on your computer.")
        ProgramFilePath = input("Installer>")
        if ProgramFilePath.lower() == "exit":
            print("Exited...")
            return
        print("Would you like to install by copying or moving the program file? (m) for move and (c) for copy")
        TypeOfInstall = input("Installer>").lower()
        if TypeOfInstall == "m":
            if InstallProgram(ProgramFilePath, "move"):
                print("Move Installed succesfully")
            else:
                continue
        elif TypeOfInstall == "c":
            if InstallProgram(ProgramFilePath, "copy"):
                print("Copy Installed succesfully")
            else:
                continue
        else:
            errormanager.error("user", "Not a valid command.")
            continue

        print("Would you like to install another program? (y or n)?")
        while True:
            choice = input("Installer>").lower()
            if choice == "y":
                InstallProgramUI()
            elif choice == "n":
                return
            else:
                errormanager.error("user", "Not a valid command.")

#GetProgramInfo
def GetProgramInfo(program_Name):
    try:
        with open(os.path.join("System", "Programs", program_Name, "README.md"), "r") as ReadMe:
            print(f"{program_Name} Info: {ReadMe.read()}")
    except:
        errormanager.error("user", "No Info Found. This program does not have a README.md file.")

def GetProgramInfoUI():
    ProgramList = GetProgramList()
    print("Programs:")
    for counter, programs in enumerate(ProgramList, start=1):
        print(f"{counter}.{programs}")
    print("What program would you like to get info from? IMPORTANT the program must have a README.md file or else it will return no info")
    while True:
        Progrm = input("Info>")
        if Progrm.lower() == "exit":
            print("Exited...")
            return
        if Progrm in ProgramList:
            GetProgramInfo(Progrm)
            return
        else:
            try:
                programIndex = int(Progrm)
                if ProgramList[programIndex - 1] != "" or ProgramList[programIndex - 1] != None:
                    GetProgramInfo(ProgramList[programIndex - 1])
                    return
            except:
                errormanager.error("user", "Program does not exist.")

#Delete Programs
def DeleteProgram(program_Name):
    path = os.path.join("System", "Programs", program_Name)
    try:
        shutil.rmtree(path)
        print("Program Deleted Successfully")
        return
    except Exception as error:
        errormanager.error("system", f"Program Failed to Delete. Advanced error: {error}")
        return

def DeleteProgramUI():
    ProgramList = GetProgramList()
    print("Programs:")
    for counter, programs in enumerate(ProgramList, start=1):
        print(f"{counter}.{programs}")
    print("What program would you like to delete? IMPORTANT program can't be recovered!")
    while True:
        Progrm = input("Deleter>")
        if Progrm.lower() == "exit":
            print("Exited...")
            return
        if Progrm in ProgramList:
            DeleteProgram(Progrm)
            return
        else:
            try:
                programIndex = int(Progrm)
                if ProgramList[programIndex - 1] != "" or ProgramList[programIndex - 1] != None:
                    DeleteProgram(ProgramList[programIndex - 1])
                    return
            except:
                errormanager.error("user", "Program does not exist.")

#Program Manager Main UI
def ProgramManagerMain():
    SystemActions.ShowArt("ProgramManagerLogo.txt")
    print("Welcom to Program Manager. This allows you to install, run, and delete are program files.")
    print("1.Run Program")
    print("2.Install Program")
    print("3.Program Info")
    print("4.Delte Program")
    print("5.Exit Program Manager")
    while True:
        Command = input("ProgramManager>").lower()
        if Command == "1" or Command == "run program":
            RunProgramUI()
        elif Command == "2" or Command == "install program":
            InstallProgramUI()
        elif Command == "3" or Command == "program info":
            GetProgramInfoUI()
        elif Command == "4" or Command == "delte program":
            DeleteProgramUI()
        elif Command == "5" or Command == "exit" or Command == "exit program manager":
            print("Exited...")
            return
        else:
            errormanager.error("user", f"{Command} is Not a valid command.")