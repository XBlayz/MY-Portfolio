# v1.3
Running the application with the argument `-roll {dice}` will immediately return the result of the dice expression.
If instead using `-roll-multi {dice}` it will return the list of dice rolled with the result.

# v1.2
When rolling multiple dice display all the dice results.

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