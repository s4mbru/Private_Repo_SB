import time

def main():

    from BirdBrain import Finch
    finch = Finch('A') #Initializing the finch
    done = False #Boolean variable to end while loop when user is finished
    speed = 20 #Constant for finch speed
    distance = 100 #Constant for diatance finch moves
    
    startupDisplay(finch)

    #While loop to keep taking user input until user is finished with finch
    while not done:
        print("1 = Draw line") #Display option 1 
        print("2 = Draw wavy line") #Display option 2
        print("3 = Draw triangle") #Display option 3
        print("4 = Draw circle") #Display option 4
        print("5 = Weather report") #Add the temperature functions later
        print("6 = Finch moves forward") #Display forward movement
        print("7 = Finch turns to the right") #Display turn right movement
        print("8 = Finch turns to the left") #Display turn left movement
        print("9 = Finch turns around") #Display turn around movement
        num = input("Enter your choice: ") #Take user input to determine action

        if num == "1":
            drawLine(finch, speed, distance) #Calls the line function to draw shape
        elif num == "2":
            drawWavyLine(finch, speed, distance) #Calls the wavy line function to draw shape
        elif num == "3":
            drawTriangle(finch, speed, distance) #Calls the triangle function to draw shape
        elif num == "4":
            drawCircle(finch, speed, distance) #Calls the circle function to draw shape
        elif num == "5":
            reportWeather(finch) #Calls the weather function to obtain temperature
        elif num == "6":
            finch.setMove('F', speed, distance) #Finch moves forward turning 
                                                #inputs only turn and don't move forward
        elif num == "7":
            finch.setMove('R', 92, 30)#Finch turns 90 degrees to the right
        elif num == "8":
            finch.setTurn('L', 90, 30)#Finch turns 90 degrees to the left
        elif num == "9":
            finch.setTurn('R', 180, 30)#Finch turns 180 degrees to the right to turn the opposite direction
        else:
            print("Invalid input!") #Testcase for all other inputs

        done = input("Do you want to exit? True/False: ").lower() == "true" #Ask if user wants to end loop
    
    whenDone(finch) #Calls to print finished message on terminal and display LED face
    finch.stopAll() #Ends system

#User should press button on app to alert that they are done drawing.
#As they press that buttton on the app, they should be pressing
#the A or B button on the LED board to get feedback on their art
def whenDone(finch):
    
    #Two different messages that could be displayed
    message1= "BEAUTIFUL!"
    message2= "AMAZING!!"
    
    #Message displayed on LED board when A button is pressed
    if(finch.getButton('A')):
        finch.print(message1)
    #Message displayed on LED board when B button is pressed
    if(finch.getButton('B')):
        finch.print(message2)

    endDisplay(finch) #Calls method to display LED face

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

#Use .playNote() to play a little scale
#when the Finch finishes drawing a designated shape
def finishDrawingCelebration(finch):

    finch.playNote(60,0.5)# C4, middle C
    finch.playNote(61,0.5)# C#4
    finch.playNote(62,0.5)# D4
    finch.playNote(63,0.5)# D#4
    finch.playNote(64,0.5)# E4
    finch.playNote(65,0.5)# F4
    finch.playNote(66,1)# F#4

# Shape methods
# --------------

#Finch draws a line
def drawLine(finch, speed, distance):

    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forward
    finishDrawingCelebration(finch)

#Finch draws a wavy line
def drawWavyLine(finch, speed, distance):

    obsCheck(finch)
    finch.setMotors(0, 60) #Sets motor/wheel speed of finch
    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forward
    obsCheck(finch)
    finch.setTurn('R', 360, 30) #Finch turns 360 degrees right
    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forawrd
    finishDrawingCelebration(finch)

#Finch draws a triangle
def drawTriangle(finch, speed, distance):

    speed = 8
    distance = 50
    
    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forward
    obsCheck(finch)
    finch.setTurn('R', 120, distance) #Finch turns 120 degrees right
    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forward
    obsCheck(finch)
    finch.setTurn('R', 125, distance) #Finch turns 125 degrees right
    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forward
    finishDrawingCelebration(finch)

#Finch draws a circle
def drawCircle(finch, speed, distance):

    obsCheck(finch)
    finch.setTurn('R', 360, distance) #Finch turns 360 degrees right
    finishDrawingCelebration(finch)

# Weather Sensor Methods
# -----------------------------

#Uses Finch's inherited micro:bit temperature sensor
def getWeather(finch):

    temp = finch.getTemperature() #Use finch sensor to obtain temeperature of room
    return temp

#Local classification based on temperature
def classifyWeather(temp):
    
    if temp <= -1: #If less than 30F/-1C, temperature is cold
        return "cold"
    elif temp > -1 and temp <= 15: #If less greater than 30F/-1C but less than 60F/15C, temperature is warm
        return "warm"
    else: #If greater than 60F/15C, temperature is hot
        return "hot"

#Displays light color based on weather temperature (Mess around with later)
def weatherLights(finch, wtype):
    
    if wtype == "cold":
        finch.setBeak(0, 0, 100) #When cold, turn beak blue
        finch.setTail("all", 0, 0, 100) #May change later
    elif wtype == "warm":
        finch.setBeak(0, 100, 0) #When warm, turn yellow/orange
        finch.setTail("all", 0, 100, 0) #May change later
    else:
        finch.setBeak(100, 0, 0) #When hot, turn red
        finch.setTail("all", 100, 0, 0) #May change later

#Finch tweets depending on weather (Mess around with later/May just remove feature)
def weatherSound(finch, wtype):

    if wtype == "cold":
        finch.playNote(50, 0.5) #Plays a note to signify cold weather (May change)
        finch.playNote(45, 0.5)
    elif wtype == "warm":
        finch.playNote(60, 0.5) #Plays a note to signify cold weather (May change)
        finch.playNote(64, 0.5)
    else:
        finch.playNote(72, 0.5) #Plays a note to signify cold weather (May change)
        finch.playNote(76, 0.5)

#Displays temperature on finch (Scrolling text)
def reportWeather(finch):

    # Get data
    temp = getWeather(finch)
    wtype = classifyWeather(temp)

    # Console output
    print("Temperature:", temp, "C")
    print("Weather classification:", wtype)

    # Display output on finch
    weatherLights(finch, wtype)
    # weatherSound(finch, wtype)
    message = f"{wtype} {temp}C"
    finch.print(message)

#Object Sensor Method
#--------------------

#Method detects if an object is in front of the finch and
#moves away from it using the distance sensor
def obsCheck(finch):

    dist = finch.getDistance()

    while(dist < 30):
    #If an object is in front of the finch the finch's beak will become red and
    #play an F# in the sixth octave to alert
    #user that there is an object that needs to be moved from the art space
        finch.playNote(90,1)
        finch.setBeak(100,0,0)
        finch.setTurn('L', 90, 50) #Finch turns left
        dist = finch.getDistance()

    #Resets finch tail to no color when it is no longer blocked by an object
    finch.setBeak(0,0,0)

if __name__ == "__main__":
    main()
