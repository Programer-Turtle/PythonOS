import os

def InstallErrorManagerBackup():
    try:
        with open(os.path.join("System", "Repair", "ErrorManager.PyOSRe"), "r") as BackUpCode:
            with open(os.path.join("System", "errormanager.py"), "w") as Backup:
                Backup.write(BackUpCode.read())
                return
    except Exception as e:
        print(f"Repair failed. Backup may be missing. If not try again. Advanced Error: {e}")

def InstallSystemActionsBackup():
    try:
        with open(os.path.join("System", "Repair", "SystemActions.PyOSRe"), "r") as BackUpCode:
            with open(os.path.join("System", "SystemActions.py"), "w") as Backup:
                Backup.write(BackUpCode.read())
                return
    except Exception as e:
        print(f"Repair failed. Backup may be missing. If not try again. Advanced Error: {e}")
    
def InstallProgramManagerBackup():
    try:
        with open(os.path.join("System", "Repair", "ProgramManager.PyOSRe"), "r") as BackUpCode:
            with open(os.path.join("System", "Programs", "ProgramManager.py"), "w") as Backup:
                Backup.write(BackUpCode.read())
                return
    except Exception as e:
        print(f"Repair failed. Backup may be missing. If not try again. Advanced Error: {e}")