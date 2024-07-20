from Robot import Robot
	
def main():
	robot = Robot()
	robot.parseRobotInput("PLA")
	robot.parseRobotInput("PLACE 2,4,SOUTH")
	robot.parseRobotInput("REPORT")
	robot.parseRobotInput("PLACE 3,1,e")
	robot.parseRobotInput("REPORT")
	robot.parseRobotInput("MOVE")
	robot.parseRobotInput("REPORT")
	robot.parseRobotInput("RIGHT")
	robot.parseRobotInput("LEFT")
	robot.parseRobotInput("LEFT")
	robot.parseRobotInput("REPORT")
	robot.parseRobotInput("MOVE")
	robot.parseRobotInput("MOVE")
	robot.parseRobotInput("MOVE")
	robot.parseRobotInput("REPORT")
	robot.parseRobotInput("MOVE")
	robot.parseRobotInput("REPORT")

	while True:
		userInput = input()
		robot.parseRobotInput(userInput)
  
def executeFromFile(filePath : str):
	'''
	Creates a new Robot instance and executes the commands
	from the given file
	
	Parameters:
		filePath (str): The filepath of the file to be read
	'''
	with open(filePath, "r") as file:
		robot = Robot()
		while(line := file.readline().strip()):
			robot.parseRobotInput(line)
	
if __name__ == "__main__":
	main()