from Direction import Direction

class Robot:
	__x: int = 0
	__y: int = 0
	__direction: Direction = Direction.NORTH
	__isPlaced: bool = False
		
  
	def parseRobotInput(self, command:str):
		'''
		Parse a command given by the user and apply it to this robot instance.
		
		Parameters:
			command (str): The command to be parsed.
		'''
		if command[0:6]=="PLACE ":
			#Parse inputs from format: PLACE X,Y,F
			parameters = command[6:].split(",")
			if len(parameters)!=3:
				print("Not enough parameters, PLACE requires X,Y,F")
				return
			x = int(parameters[0])
			y = int(parameters[1])
			f = parameters[2]
   
   			#Sanitise inputs
			if not Robot.__validatePosition(x, y):
				print("Position Invalid - X and Y must both be in the range of 0 to 4 inclusive")
				return
			try:
				direction = Direction[f]
    			#Update all variables atomically upon validation completion
				self.__x = x
				self.__y = y
				self.__direction = direction
				self.__isPlaced = True
			except KeyError:
				print("Direction Invalid - The direction must be one of NORTH,EAST,SOUTH,WEST")
			return
   
		if not self.__isPlaced:
			print("Ignoring command - PLACE must be called first")
			return
   
		match(command):
			case("MOVE"):
				self.__move()
			case("LEFT"):
				self.__direction = self.__direction.rotateLeft()
			case("RIGHT"):
				self.__direction = self.__direction.rotateRight()
			case("REPORT"):
				self.__report()
			case("_"):
				print("Invalid command")


	def __move(self):
		'''
		Move the robot forward one space in the direction it is facing.
		The robot will not move if doing so would result in it falling
		off the table.
		'''
		moveX, moveY = self.__direction.movementCoords()
		newPosition = [self.__x + moveX, self.__y + moveY]
		if Robot.__validatePosition(*newPosition):
			self.__x, self.__y = newPosition
  
  
	def __validatePosition(x: int,y: int) -> bool:
		'''
		Validates the given position is within the bounds of the table
  
		Parameters:
			x (int): The x co-ordinate
   			y (int): The y co-ordinate
   
   		Returns:
			A boolean representing if the x and y co-ordinates are valid
		'''
		return not (x<0 or x>4 or y<0 or y>4)
			
   
	def __report(self):
		'''
		Private method to output the current x,y position and the direction
  		currently being faced.
  		'''
		print(f"{self.__x}, {self.__y}, {self.__direction.name}")