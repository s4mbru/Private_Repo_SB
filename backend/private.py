from BirdBrain import Finch
import time

def main():

    finch = Finch('A') #Initializing the finch
    done = False #Boolean variable to end while loop when user is finished
    speed = 20 #Constant for finch speed
    distance = 100 #Constant for diatance finch moves
    
    finch.startupDisplay(finch)
    print("1 = Draw line") #Display option 1 
    print("2 = Draw wavy line") #Display option 2
    print("3 = Draw triangle") #Display option 3
    print("4 = Draw circle") #Display option 4
    'print("5 = Weather report")' #Add the temperature functions later
    num = int(input("Enter your choice: ")) #Take user input to determine action

    #While loop to keep taking user input until user is finished with finch
    while done != True:
        if num == 1:
            drawLine(speed, distance) #Calls the line function to draw shape
        elif num == 2:
            drawWavyLine(speed, distance) #Calls the wavy line function to draw shape
        elif num == 3:
            drawTriangle(speed, distance) #Calls the triangle function to draw shape
        else:
            drawCircle(speed, distance) #Calls the circle function to draw shape
        '''else:
            weatherReport(finch)''' #Add the temperature functions later
        done = boolean(input("Do you want to exit? True/False: ")) #Ask if user wants to end loop

    endDisplay(finch) #Calls function to display disconnecting LED face
    finch.stopAll() #Ends system

#LED display at start of every drawing phase
def startupDisplay(finch):

    #Turn each number in position into constant later
    finch.setDisplay([
        0, 1, 0, 1, 0,
        0, 1, 0, 1, 0,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        0, 1, 1, 1, 0
    ])
    time.sleep(1) #Stops system

#LED display at end of program
def endDisplay(finch):

    #Turn each number in position into constant later
    finch.setDisplay([
        1, 1, 0, 1, 1,
        0, 0, 0, 0, 0,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        0, 1, 1, 1, 0
    ])
    time.sleep(1) #Stops system

#Finch dances/sings after it completes its given task (Work on later)
def finishDrawingCelebration(speed, distance):

    finch.setMove('F', speed, distance)

# Shape methods
# --------------

#Finch draws a line
def drawLine(speed, distance):

    finch.setMove('F', speed, distance) #Finch moves forward
    finch.playNote(60, 1) #Plays note when finished with task(Change into constant later)
    finch.finishDrawingCelebration(speed, distance) #Fix later

#Finch draws a wavy line
def drawWavyLine(speed, distance):

    finch.setMotors(0, 60) #Sets motor/wheel speed of finch
    finch.setMove('F', speed, distance) #Finch moves forward
    finch.setTurn('R', 360, 30) #Finch turns 360 degrees right
    finch.setMove('F', speed, distance) #Finch moves forawrd
    finch.finishDrawingCelebration(speed, distance) #Fix later

#Finch draws a triangle
def drawTriangle(speed, distance):

    speed = 8
    distance = 50
    
    finch.setMove('F', speed, distance) #Finch moves forward
    finch.setTurn('R', 120, distance) #Finch turns 120 degrees right
    finch.setMove('F', speed, distance) #Finch moves forward
    finch.setTurn('R', 125, distance) #Finch turns 125 degrees right
    finch.setMove('F', speed, distance) #Finch moves forward
    finch.finishDrawingCelebration(20, 100) #Fix later

#Finch draws a circle
def drawCircle(speed, distance):
    
    finch.setTurn('R', 360, distance) #Finch turns 360 degrees right
    finch.finishDrawingCelebration(20, 100) #Fix later
