from asyncio import subprocess
from rich import print
from rich.prompt import Prompt
from time import sleep
from os import system

def selscreen():
    system('clear')    
    print("""[red]
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ███████╗███████╗ ██████╗ ███╗   ██╗
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ╚══███╔╝██╔════╝██╔═══██╗████╗  ██║
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║         ███╔╝ █████╗  ██║   ██║██╔██╗ ██║
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║        ███╔╝  ██╔══╝  ██║   ██║██║╚██╗██║
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ███████╗███████╗╚██████╔╝██║ ╚████║
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝                                                                                  

Please select a option from the menu below:

1: Check the time and date.
2: Launch the terminal.
3: Check the weather. [Not working.]
4: Check the current IP being used.
5: Install pip packages. [Use spaces to seperate packages.]
6: Install apt packages. [Use spaces to seperate packages | LINUX ONLY!]
7: Run linux apt packages. [LINUX ONLY!]
""")

    choice = Prompt.ask("[red]Please enter your choice: ")

    choices = ['1', '2', '3', '4', '5', '6', '7']

    if choice not in choices:
        print("[red]Please enter a valid choice.")
        sleep(2)
        selscreen()
    else:
        if choice == '1':
            print("[red]The date and time is:")
            system('date')
            sleep(2)
            selscreen()
        if choice == '2':
            animation = 'Launching terminal......\n'
            
            for chars in animation:
                print("[red]{}".format(chars), end='')
                sleep(0.15)
        if choice == '3':
            print("[red]This feature is not working yet.")
            sleep(2)
            selscreen()
        if choice == '4':
            import subprocess as sp
            print("[red]The current IP address is:")
            ip = sp.getoutput('curl ifconfig.me')
            ip = ip.split('\n')[-1]
            print('[red]{}'.format(ip))
            sleep(2)
            selscreen()
        if choice == '5':
            packages = Prompt.ask("[red]Enter packages you would like to install [list multiple packages with a space]: ")
            for package in packages:
                print("[red]Installing {}...".format(package))
                sleep(1)
                system('pip3 install {}'.format(package))
            sleep(2)
            selscreen()
        if choice == '6':
            packages = Prompt.ask("[red]Enter packages you would like to install [list multiple packages with a space]: ")
            print("[red]Attempting to install packages...")

            try:
                system('apt-get install {}'.format(packages))
            except:
                print("[red]Please run this command as root.")
                sleep(2)
                selscreen()
            sleep(2)
            selscreen()
        if choice == '7':
            package = Prompt.ask("[red]Enter package you would like to run: ")
            print('[red]Please note: You must run this command as root and make sure the package is installed otherwise you will get a error like: /bin/sh: x not fount.')

            try:
                system(f'{package}')
                sleep(2)
                selscreen()
            except:
                print("[red]Please run this command as root.")
                sleep(2)
                selscreen()

selscreen()
