from lib.BirdBrain import Finch

finch = Finch('A')
finch.setMove('F', 100, 100)
finch.setTurn('R', 360, 30)

finch.setBeak(0, 100, 0)
finch.setDisplay([0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setMove('F',10, 50)
finch.setDisplay([1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
