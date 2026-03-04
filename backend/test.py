from BirdBrain import Finch

finch.setDisplay([0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setDisplay([1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch = Finch('A')
shape = int(input())
if shape == 1:
    #Draw line
    finch.setMove('F', 20 ,100)
    finch.playNote(60, 0.5)
elif shape == 2:
    #Draw wavy line
    finch.setMove('F', 20 ,100)
    finch.setTurn('R', 360, 30)
    finch.setMove('F', 20 ,100)
    finch.playNote(60, 0.5)
elif shape == 3:
    #Draw triangle
    finch.playNote(60, 0.5)
else:
    #Draw circle
    finch.playNote(60, 0.5)
finch.setMove('F', 20 ,100)
finch.setTurn('R', 360, 30)
finch.playNote(60, 0.5)
finch.setMove('F', 20, 100)
finch.setTurn('R', 360, 30)
finch.playNote(70, 0.5)
