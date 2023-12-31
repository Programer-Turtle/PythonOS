# Python OS

Hello welcome to Python OS. This program has some scripts from python like the ascii art and the preinstalled adventure game. This program has the capability to run python code. In the future we plan to add file handling. If you need help type '?' or 'help'. Feel free to modify Python OS to make your own.

# How to use
Open the "PythonOS.py" file. Makr sure you have the latest version of python installed.

# Main File
Used to navigate through commands and other programs

- **Commands**:
- `help/?` - Gives a list of all the commands and what they do.
- `cls/clear` - Clears all text off the screen.
- `about` - Clears all text off the screen and shows the about page. Happens automaticaly at boot.
- `color` - Sets color of the terminal text and saves color for next boot. Example: [Input:color 0a] [Output:Terminal color is green]
- `ProgramManager` - Opens the program manager
- `shutdown` - Shuts down Python OS

Extra Tips:
- You can also type in installed program's names to run them.
- Most actions can be exited by typing 'exit'.

# Program Manager
Used to run, install, get info from, and delete programs.

1. **Run Program** Runs program selcted from list.
2. **Install Program** Installs program to system from computer using directories path. Any program must have a "index.py" file for it to run in PythonOS
3. **Program Info** Shows the Read me file in a program selcted from a list. Program must have a "README.md" file for it to work.
4. **Delete Program** Deletes a program selected from a list.
5. **Exit Program Manager** Closes Program Manager and goes back to the normal interface of Python OS

# Preinstalled Programs
- `AdventureGame` A basic terminal based adventure game. Credits to https://github.com/the-coding-pie/text-based-adventure-game-python
- `ChatBot` A basic chat bot.
- `NameCheck` A basic script that allows you to compare names to an unfinished name.
- `NameScrambled` A basic script that allows you to scramble a list of names.
- `NameUnscramble` A basic script tha allows to check if a scrambled name is part of a list of unscrambled names. 

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
It contians backups of the code for some system files. It can use these backups to restore files if missing.

**backed up files**
- `SystemActions.py`
- `errormanager.py`
- `ProgramManager.py`