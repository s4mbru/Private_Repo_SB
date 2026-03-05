from BirdBrain import Finch

finch = Finch('A')
shape = int(input())
if shape == 1:
    #Draw line
    finch.setMove('F', 20 ,100)
    finch.playNote(60, 0.5)
#Draw wavy line
finch.setMove('F', 20 ,100)
finch.setTurn('R', 360, 30)
finch.playNote(60, 0.5)
finch.setMove('F', 20 ,100)
finch.setTurn('R', 360, 30)
finch.playNote(60, 0.5)
finch.setMove('F', 20, 100)
finch.setTurn('R', 360, 30)
finch.playNote(70, 0.5)
