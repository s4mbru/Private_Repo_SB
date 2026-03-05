from lib.BirdBrain import Finch
import time

finch = Finch('A')

#Makes a line
finch.setMotors(10,10)
finch.setMove('F',30, 50)
finch.setMove('F',20, 50)

#Makes a triangle
finch.setMove('F',8, 50)
finch.setTurn('R',120, 50)
finch.setMove('F',8, 50)
finch.setTurn('R',125, 50)
finch.setMove('F',8, 50)
finch.setMove('F',10, 50)
