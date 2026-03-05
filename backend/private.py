from lib.BirdBrain import Finch
import time

finch = Finch('A')

#Makes a line
finch.setDisplay([0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setMove('F',20,50)
finch.playNote(60,0.5)
finch.setDisplay([1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setMove('F',10,50)

#Makes a triangle
finch.setDisplay([0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setMove('F',8,50)
finch.setTurn('R',120,50)
finch.setMove('F',8,50)
finch.setTurn('R',125,50)
finch.setMove('F',8,50)
finch.playNote(60,0.5)
finch.setDisplay([1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setMove('F',10,50)

#Makes a circle
finch.setDisplay([0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setMotors(0,100)
time.sleep(3)
finch.stop()
finch.playNote(60,0.5)
finch.setDisplay([1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setMove('F',10,50)

#Makes a wavy line
finch.setDisplay([0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
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
finch.playNote(60,0.5)
finch.setDisplay([1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
