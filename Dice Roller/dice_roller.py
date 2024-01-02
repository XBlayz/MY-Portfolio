"""Dice Roller CLI interface

Can roll dice by interpreting command using a simple CLI interface.
"""

__version__ = '1.1'
__author__ = 'XBlayz'

import os
import sys
import random
from datetime import datetime

def decode_cmd(cmd:str) -> dict[str, any]:
    """Decode the string 'cmd' returning a dictionary structured as {"CMD": str, "Value": any}:
    - CMD: is the name of the command decoded;
    - Value: is the optional value of the command;
    """

    # help|h
    if cmd in ["help","h"]:
        s = "List of command:\n"
        s += "- <n:int>d<m:int>[+<v:int>]: <n> dice of <m> face, optionally adding <v> as a modifier\n"
        s += "- clear, cls: clear history on screen\n"
        s += "- exit, esc: close the application\n"
        return {"CMD": "__HELP__", "Value": s}

    # clear|cls
    elif cmd in ["clear","cls"]:
        return {"CMD": "__CLEAR__", "Value": None}

    # exit|esc
    elif cmd in ["exit","esc"]:
        return {"CMD": "__EXIT__", "Value": None}

    # <n:int>d<m:int>[+<v:int>]
    else:
        value = roll_dice_list(cmd)
        if isinstance(value, str):
            return {"CMD": "__ERROR__", "Value": value}
        else:
            return {"CMD": "__DICE__", "Value": value}

def roll_dice(cmd:str) -> any:
    """Decode the string 'cmd' returning the rolled value or the error message."""

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
        for _ in range(n):
            r += random.randrange(1, m+1)

        # Return result
        return r

    # Invalid command
    except IndexError :
        return f"'{cmd}' is an invalid command"
    
    # Invalid number
    except ValueError as e:
        SEP = "'"
        return f"Invalid number '{e.args[0].split(SEP)[-2]}'"

def roll_dice_list(cmd:str) -> any:
    """Decode the string 'cmd' returning a list of the rolled value or the error message."""

    try:
        cmd_l = cmd.replace(" ", "").split("d")
        if len(cmd_l) == 1:
            raise(IndexError)

        # Decode numbers
        n = int(cmd_l[0])
        if cmd_l[1].count("+") > 0:
            mod_l = cmd_l[1].split("+")

            m = int(mod_l[0])
            r = [int(mod_l[1])]
        else:
            m = int(cmd_l[1])
            r = []

        # Calculate random numbers
        for _ in range(n):
            r.insert(0, random.randrange(1, m+1))

        # Return result
        return r

    # Invalid command
    except IndexError :
        return f"'{cmd}' is an invalid command"
    
    # Invalid number
    except ValueError as e:
        SEP = "'"
        return f"Invalid number '{e.args[0].split(SEP)[-2]}'"

def print_dice(dice: list[int]) -> None:
    r = 0
    print("[", end="")
    for i in range(len(dice)):
        r += dice[i]
        if i+1 < len(dice):
            print(f"{dice[i]}+", end="")
        else:
            print(f"{dice[i]}] = ", end="")
    print(f"{r}")

def main() -> None:
    # Set random seed
    random.seed(datetime.now().timestamp())

    # Run CLI
    os.system('cls')
    while True:
        # Wait input
        cmd = input("> ")

        # Execute commands
        cmd_dict = decode_cmd(cmd)
        match cmd_dict["CMD"]:
            case "__HELP__":
                print(cmd_dict["Value"])
            case "__CLEAR__":
                os.system('cls')
            case "__EXIT__":
                os.system('cls')
                break
            case "__DICE__":
                if len(cmd_dict["Value"]) == 1:
                    print(cmd_dict["Value"][0])
                else:
                    print_dice(cmd_dict["Value"])
            case "__ERROR__":
                print(cmd_dict["Value"])

if __name__ == "__main__":
    if len(sys.argv) > 2:
        if sys.argv[1] == "-roll":
            print(roll_dice(sys.argv[2]))
        elif sys.argv[1] == "-roll-multi":
            print_dice(roll_dice_list(sys.argv[2]))
        else:
            main()
    else:
        main()