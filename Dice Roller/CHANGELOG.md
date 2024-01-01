# v1.1
Reformatted code with function structure.
Can be used as a module by calling the function `roll_dice(cmd:str) -> any` for evaluating a dice command.

# v1.0
CLI interface command list:
* **<n:int>d<m:int>[+<v:int>]**:
    * *n*: is the number of dice to roll;
    * *m*: is the number of faces on each die;
    * *v*: is a modifier added to the result;
* **Help**: explain all the possible commands;
* **Clear**: clear the history on the screen;
* **Exit**: close the application;