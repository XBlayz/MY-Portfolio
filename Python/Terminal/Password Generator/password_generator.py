"""Password generator terminal application

Will return a random password with the specified characteristics by running this application in the terminal with different arguments.
"""

__version__ = '1.0'
__author__ = 'XBlayz'

import sys
import random
from datetime import datetime

def password(l:int, uc:bool, sc:bool) -> str:
    s = ""
    for _ in range(l):
        n = random.randrange(0,3)
        if (not sc) and n == 2:
            n -= 1
        if (not uc) and n == 1:
            n -= 1
        
        s += random_c(n)
    return s

def random_uc() -> str:
    return str(chr(random.randrange(65,91)))

def random_lc() -> str:
    return str(chr(random.randrange(97,123)))

def random_sc() -> str:
    return random.choice(["!","@","#","&","%","?","^"])

def random_c(n:int) -> str:
    match n:
        case 0:
            return random_lc()
        case 1:
            return random_uc()
        case 2:
            return random_sc()

def main(argv:list[str]) -> None:
    # Set random seed
    random.seed(datetime.now().timestamp())

    l = 10
    uc = False
    sc = False

    i = 0
    while i < len(argv):
        match argv[i]:
            case "-l":
                try:
                    i+=1
                    l = int(argv[i])
                except:
                    print("Error!")
                    return
            case "-uc":
                uc = not uc
            case "-sc":
                sc = not sc
            case _:
                print("Error!")
                return
        i+=1

    print(password(l, uc, sc))

if __name__ == "__main__":
    main(sys.argv[1:])