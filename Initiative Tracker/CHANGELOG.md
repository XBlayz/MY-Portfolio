# v1.0.1
Fixed sorting.

# v1.0
Display the tracking table on top, waiting for command to execute and updating the table.
CLI interface command list:
* **Add <name:str> <intve:int>|{dice} [<hp:int>] [<ac:int>]**: add a row with the *name* and optional *hp* and *ac*, for the initiative you can put an integer *intve* or *roll a dice* (using the [dice expression](../Dice%20Roller/CHANGELOG.md));
* **Remove <name:str>**: remove the row with then *name* selected;
* **HP <name:str> <hp:int>**: add *hp* (also negative number) to the row named *name*;
* **AC <name:str> <ac:int>**: set the *ac* to the row named *name*;
* **Next**: advance to the next turn;
* **Reset**: reset the table and the round;
* **Help**: explain all the possible commands;
* **Exit**: close the application;