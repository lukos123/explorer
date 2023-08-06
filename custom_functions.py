import os
import time

import shutil
from generate_javascript import generate_javascript
from subprocess import call
import stat
import subprocess
import psutil
import keyboard
def on_rm_error(func, path, exc_info):
        os.chmod(path, stat.S_IWRITE)
        os.unlink(path)
class Colors:
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

# Modify your ls function to use ANSI escape codes for coloring
def ls(command, now_directory, minus):
    dirs = []
    files = []
    try:
        for i in os.listdir(now_directory):
            pathToDir = os.path.join(now_directory, i)
            if i != '.git':
                if os.path.isdir(pathToDir):
                    dirs.append([pathToDir, i])
                else:
                    files.append([pathToDir, i])
        for i in files:
            print(f'{Colors.GREEN}{minus}{Colors.CYAN}{i[1]}{Colors.RESET}')
        for i in dirs:
            print(f'{Colors.GREEN}{minus}{Colors.YELLOW}{i[1]}{Colors.RESET}')
            if len(command) == 2 and command[1] == 'a':
                ls(command, i[0], '    ' + minus)
    except Exception as p:
        pass


def git(command_global, path_to_git):
    command = []

    for i in command_global:
        if len(command_global) == 1:
            command.append('git')
            break
        if i != 'git':

            command.append(i)

    if command[0] == 'add':
        os.system(f'{path_to_git} add .')
        os.system(f'{path_to_git} status')
    elif command[0] == 'init':
        os.system(f'{path_to_git} init')
        os.system(f'echo "# {command[1]}" >> README.md')
        os.system(f'echo "" >> .gitignore')
    else:
        command_end = f'{path_to_git} '
        for i in command:
            command_end += f'{i} '

        os.system(command_end)








