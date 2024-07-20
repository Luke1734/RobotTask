from robot import Robot
	
def main():
	print("Select input method:\n1: Console Input\n2: File Input")
	while True:
		userSelection = input()
		match userSelection:
			case "1":
				executeInConsole()
			case "2":
				filename = input()
				executeFromFile(filename)
			case _:
				"Invalid selection, enter 1 or 2"
  
  
def executeInConsole():
	'''
	Creates a new Robot instance and executes the commands
	entered into the console input
	'''
	robot = Robot()
	while True:
		robot.parseRobotInput(input())
	
 
def executeFromFile(filePath : str):
	'''
	Creates a new Robot instance and executes the commands
	from the given file
	
	Parameters:
		filePath (str): The filepath of the file to be read
	'''
	try:
		with open(filePath, "r") as file:
			robot = Robot()
			while(line := file.readline().strip()):
				robot.parseRobotInput(line)
	except:
		print("Error opening file, check the given file exists")
	
 
if __name__ == "__main__":
	main()