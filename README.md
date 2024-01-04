# Python OS

Hello welcome to Python OS. This program has some scripts from python like the ascii art and the preinstalled adventure game. This program has the capability to run python code. In the future we plan to add file handling. If you need help type '?' or 'help'. Feel free to modify Python OS to make your own.

# How to use
Open the "PythonOS.py" file. Make sure you have the latest version of python installed. It can also be run in Windows terminals. WARNING this script supports all Operating Systems but the color command only runs in Windows.

# Main File
Used to navigate through commands and other programs

- **Commands**:
- `help/?` - Gives a list of all the commands and what they do.
- `cls/clear` - Clears all text off the screen.
- `about` - Clears all text off the screen and shows the about page. Happens automaticaly at boot.
- `color` - Sets color of the terminal text and saves color for next boot. Example: [Input:color 0a] [Output:Terminal color is green]. Only supported on Windows.
- `ProgramManager` - Opens the program manager
- `shutdown` - Shuts down Python OS

Extra Tips:
- You can also run installed program's names as commands to run them.
- Most actions can be exited by typing 'exit'.

# Program Manager
Used to run, install, get info from, and delete programs.

1. **Run Program** Runs program selcted from list.
2. **Install Program** Installs program to system from computer using directories path. Any program must have a "index.py" file for it to run in PythonOS
3. **Program Info** Shows the Read me file in a program selcted from a list. Program must have a "README.md" file for it to work.
4. **Delete Program** Deletes a program selected from a list.
5. **Exit Program Manager** Closes Program Manager and goes back to the normal interface of Python OS

# AutoPip
A feature that makes it easier to run programs that use moduels.

# What It Does 
Checks if program has an autopip file, and if it does it installs required moduels. using the file

# Requirements
- The file must have a "install.PyOSPip" file.
- Pip is up to date.
- It is recommended for PythonOS to be up to date aswell. 

# How To Use As Developer
- Create a file name "install.PyOSPip"
- Inside this file if you have any imported moduels that are not preinstalled put there name in the file. Every module name must be in a seperate line. If there is no moduels that need to be installed just put "None" on the first line.

# Example
`pygame`
`scipy`
`numpy`
`pandas`

# Preinstalled Programs
- `AdventureGame` A basic terminal based adventure game. Credits to https://github.com/the-coding-pie/text-based-adventure-game-python
- `ChatBot` A basic chat bot. This program runs using Chatty. Chatty GitHub: https://github.com/Programer-Turtle/Chatty
- `NameCheck` A basic script that allows you to compare names to an unfinished name.
- `NameScrambled` A basic script that allows you to scramble a list of names.
- `NameUnscramble` A basic script tha allows to check if a scrambled name is part of a list of unscrambled names. 
- `Calculator` A basic calulator that can add, subtract, multiplt, divide, and use posistive exponents. This porgram runs using Operations. Operations GitHub: https://github.com/Programer-Turtle/Operations
- `Snake Game` A basic snake game using pygame. Credits to https://github.com/rajatdiptabiswas/snake-pygame

# System Actions
Contains actions that are used system wise.

- `ClearScreen()` Clears all text on terminal screen.
- `ShowArt()` Shows text out of StyleData directory. **Usually Ascii Art**
- `ShutDown()` Shuts down Python OS.

# Error Manager
Shows either system or user errors.

- `System` Output: system error. "reason"
- `User` Output: user error. "reason"

# Fixer
It contians backups of the code for some system files. It can use these backups to restore files if missing. Files ending in ".PyOSRe" are files that contain backup code.

**backed up files**
- `SystemActions.py`
- `errormanager.py`
- `ProgramManager.py`