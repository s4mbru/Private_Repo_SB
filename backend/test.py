from BirdBrain import Finch

shape = input("Which shape should be drawn?: ")
print(shape + "has been selected!")
finch.setDisplay([0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch.setDisplay([1,1,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,1,0])
finch = Finch('A')
finch.setMove('F', 20 ,100)
finch.setTurn('R', 360, 30)
finch.playNote(60, 0.5)
finch.setMove('F', 20, 100)
finch.setTurn('R', 360, 30)
finch.playNote(70, 0.5)
