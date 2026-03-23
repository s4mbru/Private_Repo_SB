from lib.BirdBrain import Finch
import time

finch = Finch('A')

#Makes a line
finch.setMotors(10,10)
finch.setMove('F',30,50)
finch.setMove('F',20,50)

#Makes a triangle
finch.setMove('F',8,50)
finch.setTurn('R',120,50)
finch.setMove('F',8,50)
finch.setTurn('R',125,50)
finch.setMove('F',8,50)
finch.setMove('F',10,50)

#Makes a circle
finch.setMotors(0,100)
time.sleep(3)
finch.stop()
finch.setMove('F',10,50)

#Makes a wavy line
finch.setMotors(0,60)
time.sleep(1)
finch.setMotors(60,0)
time.sleep(1)
finch.setMotors(0,60)
time.sleep(1)
finch.setMotors(60,0)
time.sleep(1)
finch.setMotors(0,60)
time.sleep(1)
finch.stop()
