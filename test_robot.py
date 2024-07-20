from run_robot_task import executeFromFile
from robot import Robot
from direction import Direction

#Tests are using pytest and functions prepended by test_
#pip install pytest
###############################################################################

#Test file IO
###############################################################################
def test_validFile(capfd):
    '''
    Tests an existing file containing valid commands which should place the
    robot at 2,3 facing WEST and REPORT's that to the console.
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    executeFromFile("testCases/valid.txt")
    out, _ = capfd.readouterr()
    assert out == "2,3,WEST\n"
    
    
def test_invalidFile(capfd):
    '''
    Tests the file which doesn't exist
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    executeFromFile("testCases/invalid.txt")
    out, _ = capfd.readouterr()
    assert out == "Error opening file, check the given file exists\n"
    
    
#Test rotations
###############################################################################

def test_rotateRight(capfd):
    '''
    Tests rotating 360 degrees clockwise
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    robot = Robot()
    robot.parseRobotInput("PLACE 0,0,NORTH")
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,EAST\n"
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,SOUTH\n"
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,WEST\n"
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,NORTH\n"
    
    
def test_rotateLeft(capfd):
    '''
    Tests rotating 360 degrees anti-clockwise
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    robot = Robot()
    robot.parseRobotInput("PLACE 0,0,NORTH")
    robot.parseRobotInput("LEFT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,WEST\n"
    robot.parseRobotInput("LEFT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,SOUTH\n"
    robot.parseRobotInput("LEFT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,EAST\n"
    robot.parseRobotInput("LEFT")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "0,0,NORTH\n"
    

#Test dropped inputs before place
###############################################################################

def test_inputsDropped(capfd):
    '''
    Tests that inputs are dropped before the first valid PLACE
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    robot = Robot()
    robot.parseRobotInput("PLACE a")
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("REPORT")
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("REPORT")
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("REPORT")
    robot.parseRobotInput("RIGHT")
    robot.parseRobotInput("PLACE 1,2,SOUTH")
    robot.parseRobotInput("REPORT")
    out, _ = capfd.readouterr()
    assert out == "1,2,SOUTH\n"
    
    
#Test valid place
###############################################################################

def test_allValidPlace(capfd):
    '''
    Tests PLACE in valid positions
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    directions = [Direction.NORTH.name, Direction.EAST.name,
                  Direction.SOUTH.name,Direction.WEST.name]
    for i in range(0,5):
        for j in range(0,5):
            for k in range(0,4):
                robot = Robot()
                robot.parseRobotInput(f"PLACE {i},{j},{directions[k]}")
                robot.parseRobotInput("REPORT")
                out, _ = capfd.readouterr()
                assert out == f"{i},{j},{directions[k]}\n"
                
                
def test_edgePlace(capfd):
    '''
    Tests PLACE in all positions just outside the edge of the 5x5 table.
    Should not print anything when REPORT is called
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    directions = [Direction.NORTH.name, Direction.EAST.name,
                  Direction.SOUTH.name,Direction.WEST.name]
    for i in [-1,5]:
        for j in [-1,5]:
            for k in range(0,4):
                robot = Robot()
                robot.parseRobotInput(f"PLACE {i},{j},{directions[k]}")
                robot.parseRobotInput("REPORT")
                out, _ = capfd.readouterr()
                assert out == ""
  
#Test movement
###############################################################################             

def test_validMovement(capfd):
    '''
    Tests valid movement within the board.
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    robot = Robot()
    robot.parseRobotInput(f"PLACE 0,0,EAST")
    for i in range(4):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"{i+1},0,EAST\n"
    robot.parseRobotInput(f"LEFT")
    for i in range(4):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"4,{i+1},NORTH\n"
    robot.parseRobotInput(f"LEFT")
    for i in range(4):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"{3-i},4,WEST\n"
    robot.parseRobotInput(f"LEFT")
    for i in range(4):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"0,{3-i},SOUTH\n"
        
        
def test_invalidMovement(capfd):
    '''
    Tests invalid movement against all 4 edges.
    The completion of this test also shows that input continues working
    after an invalid input is received.
    This test works by trying to move in a direction that is out of bounds
    before moving to the adjacent position to try again there.
    Makes use of the capfd fixture of pytest for capturing console output.
    '''
    robot = Robot()
    robot.parseRobotInput(f"PLACE 0,0,SOUTH")
    for i in range(5):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"{i},0,SOUTH\n"
        robot.parseRobotInput("LEFT")
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("RIGHT")
    robot.parseRobotInput(f"LEFT")
    for i in range(5):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"4,{i},EAST\n"
        robot.parseRobotInput("LEFT")
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("RIGHT")
    robot.parseRobotInput(f"LEFT")
    for i in range(5):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"{4-i},4,NORTH\n"
        robot.parseRobotInput("LEFT")
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("RIGHT")
    robot.parseRobotInput(f"LEFT")
    for i in range(5):
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("REPORT")
        out, _ = capfd.readouterr()
        assert out == f"0,{4-i},WEST\n"
        robot.parseRobotInput("LEFT")
        robot.parseRobotInput("MOVE")
        robot.parseRobotInput("RIGHT")
    