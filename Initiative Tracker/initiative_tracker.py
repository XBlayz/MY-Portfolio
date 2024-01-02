"""Initiative Tracker CLI interface

Tool for tracking turns in RPGs in a simple CLI interface.
"""

__version__ = '1.0'
__author__ = 'XBlayz'

import os
import importlib.util
import texttable

# Import dice_roller
spec=importlib.util.spec_from_file_location("dice_roller","../Dice Roller/dice_roller.py")
dice_roller = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dice_roller)

def decode_cmd(cmd:str) -> dict[str, any]:
    """Decode the string 'cmd' returning a dictionary structured as {"CMD": str, "Value": any}:
    - CMD: is the name of the command decoded;
    - Value: is the optional value of the command;
    """

    # help|h
    if cmd in ["help","h"]:
        s = "List of command:\n"
        s += "- ...\n"
        return {"CMD": "__HELP__", "Value": s}
    
    # exit|esc
    elif cmd in ["exit","esc"]:
        return {"CMD": "__EXIT__", "Value": None}

    # reset|rst
    elif cmd in ["reset","rst"]:
        return {"CMD": "__RESET__", "Value": None}
    
    # next|nxt
    elif cmd in ["next","nxt"]:
        return {"CMD": "__NEXT__", "Value": None}

    else:
        cmd_l = cmd.split(" ")

        try:
            # add <name:str> <intve:int>|{dice} [<hp:int>] [<ac:int>]
            if cmd_l[0] == "add":
                hp = 0
                ac = 0
                if len(cmd_l) > 3:
                    hp = int(cmd_l[3])
                if len(cmd_l) > 4:
                    ac = int(cmd_l[4])

                if cmd_l[2].count("d") > 0:
                    x = int(dice_roller.roll_dice(cmd_l[2]))
                    return {"CMD": "__ADD__", "Value": [" ", x, cmd_l[1], hp, ac]}
                else:
                    return {"CMD": "__ADD__", "Value": [" ", int(cmd_l[2]), cmd_l[1], hp, ac]}

            # remove <name:str>
            elif cmd_l[0] == "remove":
                return {"CMD": "__REMOVE__", "Value": cmd_l[1]}
            
            # hp <name:str> <hp:int>
            elif cmd_l[0] == "hp":
                return {"CMD": "__HP__", "Value": [cmd_l[1], int(cmd_l[2])]}
            
            # ac <name:str> <ac:int>
            elif cmd_l[0] == "ac":
                return {"CMD": "__AC__", "Value": [cmd_l[1], int(cmd_l[2])]}

            else:
                return {"CMD": "__ERROR__", "Value": "Invalid command..."}
        except:
            return {"CMD": "__ERROR__", "Value": "Invalid command..."}

def setup_table(table:texttable.Texttable) -> texttable.Texttable:
    """Setup the table."""

    table.set_cols_align(["c", "l", "c", "r", "c"])    # Setup horizontal alignment
    table.set_cols_valign(["m", "m", "m", "m", "m"])   # Setup vertical alignment
    table.set_cols_dtype(["t", "i", "t", "i", "i"])    # Setup columns types

    table.add_rows([[" ", "Initiative", "Name", "HP", "AC"]])  # Header row

    return table

def update_table(list_pg:list, index:int) -> texttable.Texttable:
    """Update the table with the new data."""

    r = setup_table(texttable.Texttable())
    if len(list_pg) != 0:
        for i in range(len(list_pg)):
            if i != index and list_pg[i][0] != " ":
                list_pg[i][0] = " "
        list_pg[index][0] = ">"
        r.add_rows(list_pg ,False)
    
    return r

def sort_l(l:list) -> None:
    for s in range(len(l)):
        min_idx = s

        for i in range(s + 1, len(l)):
            if l[i][1] > l[min_idx][1]:
                min_idx = i

        l[s], l[min_idx] = l[min_idx], l[s]

def serach_remove(l:list, item:any, index:int) -> int:
    for pg in l:
        if pg[2] == item:
            if l.index(pg) < index:
                index -= 1
            l.remove(pg)
            input("Done...")
            return index
    input("Item not found...")
    return index

def serach_hp(l:list, item:any) -> None:
    for pg in l:
        if pg[2] == item[0]:
            pg[3] += item[1]
            input("Done...")
            return
    input("Item not found...")

def serach_ac(l:list, item:any) -> None:
    for pg in l:
        if pg[2] == item[0]:
            pg[3] = item[1]
            input("Done...")
            return
    input("Item not found...")

def main():
    round_n = 1
    index = 0
    list_pg = []

    while True:
        os.system('cls')

        # Update table
        tracking_table = update_table(list_pg, index)

        # Print table and round
        print(f"Round: {round_n}")
        print(tracking_table.draw())
        
        # Wait input
        cmd = input("> ")
        cmd_dict = decode_cmd(cmd)
        match cmd_dict["CMD"]:
            case "__ADD__":
                list_pg.append(cmd_dict["Value"])
                sort_l(list_pg)
            case "__REMOVE__":
                index = serach_remove(list_pg, cmd_dict["Value"], index)

            case "__HP__":
                serach_hp(list_pg, cmd_dict["Value"])
            case "__AC__":
                serach_ac(list_pg, cmd_dict["Value"])

            case "__NEXT__":
                index += 1
                if index+1 > len(list_pg):
                    index = 0
                    round_n += 1

            case "__RESET__":
                round_n = 1
                index = 0
                list_pg = []
            case "__HELP__":
                input(cmd_dict["Value"])
            case "__EXIT__":
                os.system('cls')
                break
            case "__ERROR__":
                input(cmd_dict["Value"])

if __name__ == "__main__":
    main()