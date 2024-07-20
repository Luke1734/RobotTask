# Robot Task
- The application is a simulation of a toy robot moving on a square tabletop, of
dimensions 5 units x 5 units.
- There are no other obstructions on the table surface.
- The robot is free to roam around the surface of the table, but is prevented
from falling to destruction. Any movement that would result in the robot falling from
the table is prevented, however further valid movement commands are still allowed.


## Commands
- PLACE X,Y,F
- MOVE
- LEFT
- RIGHT
- REPORT

PLACE will put the toy robot on the table in position X,Y and facing NORTH, SOUTH,
EAST or WEST.

MOVE will move the toy robot one unit forward in the direction it is currently facing.

LEFT and RIGHT will rotate the robot 90 degrees in the specified direction without
changing the position of the robot.

REPORT will announce the X,Y and F of the robot to stdout.

## Running
Run using `python run_robot_task.py`.

## Tests
All tests reside in the `test_robot.py` file.

Tests can be ran by executing `pytest` which itself can be installed using `pip install pytest`.