from lib.BirdBrain import Finch
import time

finch = Finch('A')

#Makes a line
finch.setMotors(10,10)
finch.setMove('F',30, 50)
finch.setMove('F',20, 50)
