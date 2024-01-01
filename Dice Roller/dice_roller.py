"""Dice Roller CLI interface

Can roll dice by interpreting command using a simple CLI interface.
"""

__version__ = '1.0'
__author__ = 'XBlayz'

import os
import random
from datetime import datetime

os.system('cls')
while True:
    # Wait input
    cmd = input("> ")

    # Set random seed
    random.seed(datetime.now().timestamp())

    # Command decoder
    if cmd in ["help","h"]:
        # Help command
        print("List of command:")
        print("- <n:int>d<m:int>[+<v:int>]: <n> dice of <m> face, optionally adding <v> as a modifier")
        print("- clear, cls: clear history on screen")
        print("- exit, esc: close the application")
    elif cmd in ["clear","cls"]:
        # Clear command
        os.system('cls')
    elif cmd in ["exit","esc"]:
        # Exit command
        os.system('cls')
        break
    else:
        try:
            cmd_l = cmd.replace(" ", "").split("d")
            if len(cmd_l) == 1:
                raise(IndexError)

            # Decode numbers
            n = int(cmd_l[0])
            if cmd_l[1].count("+") > 0:
                mod_l = cmd_l[1].split("+")

                m = int(mod_l[0])
                r = int(mod_l[1])
            else:
                m = int(cmd_l[1])
                r = 0

            # Calculate random numbers
            for i in range(n):
                r += random.randrange(1,m+1)

            # Print result
            print(r)
        except IndexError :
            # Invalid command
            print(f"'{cmd}' is an invalid command")
        except ValueError as e:
            # Invalid number
            SEP = "'"
            print(f"Invalid number '{e.args[0].split(SEP)[-2]}'")