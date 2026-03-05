from lib.BirdBrain import Finch
import time

finch = Finch('A')

#Finch moves forward
finch.setMotors(10,10)
finch.setMove('F',20, 50)
finch.setTurn('R',120, 50)
finch.setMove('F',10, 50)
