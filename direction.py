from enum import Enum
from typing import Self

class Direction(Enum):
	NORTH = 0
	EAST = 1
	SOUTH = 2
	WEST = 3
 
	coords = {
    	NORTH: [0,1],
     	EAST: [1,0],
 		SOUTH: [0,-1],
   		WEST: [-1,0]
	}
 
	def rotateRight(self) -> Self:
		'''
		Rotates the current direction by 90 degrees clockwise.
  
		Returns:
			A new Direction instance rotated 90 degrees clockwise.
		
		'''
		return Direction((self.value+1)%4)

	def rotateLeft(self) -> Self:
		'''
		Rotates the current direction by 90 degrees anti-clockwise.
  
		Returns:
			A new Direction instance rotated 90 degrees anti-clockwise.
		
		'''
		#Handle case where subtracting 1 from NORTH (0) would give a negative index
		if self==Direction.NORTH:	
			return Direction.WEST
		else:
			return Direction(self.value-1)

	def movementCoords(self) -> list[int]:
		'''
		Gets the relevant x,y translation for the current direction.
  
		Returns:
			List of length 2 containing the X and Y increments to apply to the position.
		
		'''
		return Direction.coords.value[self.value]