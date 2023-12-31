
import os


from prompt_toolkit import PromptSession, HTML
from prompt_toolkit.styles import Style as St

import subprocess
import sys

import colorama


import custom_functions
print(os.getcwd())
from MyCompleter import MyCompleter
colorama.init()


args = sys.argv


cwd = os.getcwd()
drive, _ = os.path.splitdrive(cwd)

completer = MyCompleter()
path_to_python = f'python'

path_to_pip = f'pip'
session = PromptSession(completer=MyCompleter())

path_to_git = f'git'

first_directory = args[1]

os.chdir(first_directory)


def app():
    try:
        while True:
            
                
            now_directory = os.getcwd()

            def bottom_toolbar():
                return [('class:bottom-toolbar', '         Итс май апликатион!')]
            our_style = St.from_dict({
                '':   '#0000FF bold',
                'bottom-toolbar': 'fg:#ffffff bg:#ff0000',
                # 'sw':   '#fff bold',


            })
            
            command = session.prompt(
                HTML(f"<b><yellow>{now_directory}</yellow><violet>?</violet></b>"), completer=completer,
                style=our_style, bottom_toolbar=bottom_toolbar).split()
            
            if len(command) > 0:
                now_directory = os.getcwd()
                if command[0] == 'ls':
                    custom_functions.ls(command, now_directory, '└───')
                elif command[0] == 'cd':
                    cd = ''

                    if len(command) > 2:
                        for i in range(len(command)-1):
                            cd += command[i+1]+' '

                    else:
                        cd = command[1]
                    cd = os.path.join(now_directory, cd)

                    try:
                        os.chdir(cd)
                    except:
                        print('error')
                
                
                elif command[0] == 'git':
                    custom_functions.git(command, path_to_git)
                

                else:
                    command_another = ''
                    for i in command:
                        command_another += f'{i} '
                    os.system(command_another)
    except KeyboardInterrupt:
        print('\nControl+C был нажат, но программа не выключается.')

if __name__ == '__main__':
    while True:
        try:
            app()
        except Exception as t:
            print(t)
