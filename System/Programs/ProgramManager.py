import os
import subprocess
import shutil
from .. import errormanager
from .. import SystemActions

def GetProgramList():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    # Get all files in the folder
    directories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]
    if "__pycache__" in directories:
        directories.remove("__pycache__")
    
    return directories

#Run programs
def RunProgram(program_Name):
    try:
       program_path = os.path.join("System", "Programs", program_Name, "index.py")
       with open(program_path, "r"):
           print("Program index.py file found. Running Progam")
       subprocess.run(['python', program_path])
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