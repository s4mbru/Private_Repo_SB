import time

def main():

    from lib.BirdBrain import Finch
    finch = Finch('A') #Initializing the finch
    done = False #Boolean variable to end while loop when user is finished
    speed = 20 #Constant for finch speed
    distance = 100 #Constant for diatance finch moves
    ledOff = 0 #Constant to not display LED light
    ledOn = 1 #Constant to display LED light
    
    startupDisplay(finch, ledOn, ledOff) #Calls function to display smiley face

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
        choice = input("Enter your choice: ") #Take user input to determine action

        num = getValidInput(choice)
        
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
            obsCheck(finch) #Calls obstacle check method to detect if anything is blocking Finch
            finch.setMove('F', speed, distance) #Finch moves forward turning 
                                                #inputs only turn and don't move forward
        elif num == "7":
            obsCheck(finch)
            finch.setTurn('R', 95, 30)#Finch turns 90 degrees to the right
        elif num == "8":
            obsCheck(finch)
            finch.setTurn('L', 95, 30)#Finch turns 90 degrees to the left
        elif num == "9":
            obsCheck(finch)
            finch.setTurn('R', 185, 30)#Finch turns 180 degrees to the right to turn the opposite direction
        else:
            print("Invalid input!") #Output for all inputs with no number

        choice = input("Do you want to exit?: ").lower() #Ask if user wants to end loop
        done = choice in ["true", "t", "yes", "y"]
        
    whenDone(finch) #Calls to print finished message on terminal and display LED face
    finch.stopAll() #Ends system

#Basic Helper Functions
#-----------------

def startupDisplay(finch, on, off):
    '''LED face display at start of Finch connection'''

    #Displays a smiley face on LED screen
    finch.setDisplay([
        off, on, off, on, off,
        off, on, off, on, off,
        on, off, off, off, on,
        on, off, off, off, on,
        off, on, on, on, off
    ])
    time.sleep(1) #Waits until LED face is displayed before exiting

def endDisplay(finch, on, off):
    '''LED face display at end of Finch connection'''

    #Displays a sleeping face on LED screen
    finch.setDisplay([
        on, on, off, on, on,
        off, off, off, off, off,
        on, off, off, off, on,
        on, off, off, off, on,
        off, on, on, on, off
    ])
    time.sleep(1) #Waits until LED face is displayed before exiting

def finishDrawingCelebration(finch):
    '''Use .playNote() to play a little scale
    when the Finch finishes drawing a designated shape'''

    #Note constants
    C4 = 60
    CS4 = 61
    D4 = 62
    DS4 = 63
    E4 = 64
    F4 = 65
    FS4 = 66
    shortNote = 0.5
    longNote = 1

    #Finch uses note constants to play a song
    finch.playNote(C4, shortNote)
    finch.playNote(CS4, shortNote)
    finch.playNote(D4, shortNote)
    finch.playNote(DS4, shortNote)
    finch.playNote(E4, shortNote)
    finch.playNote(F4, shortNote)
    finch.playNote(FS4, longNote)

def getValidInput(userIN):
    '''Extracts the first valid menu option from the user input'''

    #For loop to run through string and extract a valid value
    for char in userIN:
        if char in "123456789":
            return char

    #Returns nothing if input has no number
    return None

# Shape methods
# --------------

def drawLine(finch, speed, distance):
    '''Draw method that makes the Finch draw a presized line'''

    obsCheck(finch) #Calls obstacle check method to detect if anything is blocking Finch
    finch.setMove('F', speed, distance) #Finch moves forward
    finishDrawingCelebration(finch) #Finch alerts user of task completion

def drawWavyLine(finch, speed, distance):
    '''Draw method that makes the Finch draw a presized wavy line'''

    obsCheck(finch) #Calls obstacle check method to detect if anything is blocking Finch
    finch.setMotors(0,60)
    time.sleep(1)
    obsCheck(finch)
    finch.setMotors(60,0)
    time.sleep(1)
    obsCheck(finch)
    finch.setMotors(0,60)
    time.sleep(1)
    obsCheck(finch)
    finch.setMotors(60,0)
    time.sleep(1)
    obsCheck(finch)
    finch.setMotors(0,60)
    time.sleep(1)
    finch.stop()    
    finishDrawingCelebration(finch) #Finch alerts user of task completion

def drawTriangle(finch, speed, distance):
    '''Draw method that makes the Finch draw a presized triangle'''

    speed = 8
    distance = 50
    
    obsCheck(finch) #Calls obstacle check method to detect if anything is blocking Finch
    finch.setMove('F', speed, distance) #Finch moves forward
    obsCheck(finch)
    finch.setTurn('R', 120, distance) #Finch turns 120 degrees right
    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forward
    obsCheck(finch)
    finch.setTurn('R', 125, distance) #Finch turns 125 degrees right
    obsCheck(finch)
    finch.setMove('F', speed, distance) #Finch moves forward
    finishDrawingCelebration(finch) #Finch alerts user of task completion

def drawCircle(finch, speed, distance):
    '''Draw method that makes the Finch draw a presized circle'''

    obsCheck(finch) #Calls obstacle check method to detect if anything is blocking Finch
    finch.setMotors(0, 100) #Finch turns only right wheel to make circle at speed of 100
    time.sleep(2)
    finch.setMotors(0,0)
    finishDrawingCelebration(finch) #Finch alerts user of task completion

# Weather Sensor Methods
# -----------------------

def getWeather(finch):
    '''Get method that uses Finch's inherited temperature sensor
    to return the temperature within the room'''

    temp = finch.getTemperature() #Use finch sensor to obtain temeperature of room
    return temp

def classifyWeather(temp):
    '''Local classification of weather based on temperature obtained within the room'''
    
    if temp <= -1: #If less than 30F/-1C, temperature is cold
        return "cold"
    elif temp > -1 and temp <= 15: #If less greater than 30F/-1C but less than 60F/15C, temperature is warm
        return "warm"
    else: #If greater than 60F/15C, temperature is hot
        return "hot"

def weatherLights(finch, wtype):
    '''Sets Finch's tail and beak light color based on weather temperature'''
    
    if wtype == "cold":
        #When cold, turn beak and tail blue
        finch.setBeak(0, 0, 100)
        finch.setTail("all", 0, 0, 100)
    elif wtype == "warm":
        #When warm, turn beak and tail yellow/orange
        finch.setBeak(0, 100, 0)
        finch.setTail("all", 0, 100, 0)
    else:
        #When hot, turn beak and tail red
        finch.setBeak(100, 0, 0)
        finch.setTail("all", 100, 0, 0)

def reportWeather(finch):
    '''Displays temperature on Finch as scrolling text and beak and tail lights'''

    #Get weather data
    temp = getWeather(finch)
    wtype = classifyWeather(temp)

    #Temperature output displayed in console
    print("Temperature:", temp, "C")
    print("Weather classification:", wtype)

    #Display tail and beak lights and scrolling text on finch
    weatherLights(finch, wtype)
    message = f"{wtype}{temp}C"
    finch.print(message)
    time.sleep(3)
    finch.setBeak(0,0,0)
    finch.setTail("all", 0, 0, 0)

#Object Sensor Method
#---------------------

def obsCheck(finch):
    '''Method detects if an object is in front of the finch and
    moves away from it using the distance sensor'''

    #Uses sensor to obtain distance of object from Finch
    dist = finch.getDistance()

    #Alerts user that there is an object that needs to be moved from the art space
    while dist < 30:
        #Finch's beak will become red
        finch.playNote(90,1)
        #Plays an F# in the sixth octave to alert
        finch.setBeak(100,0,0)
        #Finch turns left 90 degrees
        finch.setTurn('L', 90, 50)
        #Uses sensor to detect object again
        dist = finch.getDistance()

    #Resets finch tail to no color when it is no longer blocked by an object
    finch.setBeak(0,0,0)

#A and B Button Sensor Method
#-----------------------------

def whenDone(finch):
    '''User should press button on app to signify that they are done drawing.
    After signaling that they are done, they should be pressing the A or B button on the LED board to get feedback on their art'''

    #Two different messages that could be displayed
    message1= "BEAUTIFUL!"
    message2= "AMAZING!!"

    print("Press button A or B on LED screen to get feedback!")

    while True:
        #Displays message1 button B on LED screen is pressed
        if finch.getButton('B'):
            finch.print(message1)
            time.sleep(2) #Waits until message is displayed before ending system
            break #exits while loop to continue the next step
        #Displays message2 button A on LED screen is pressed
        elif finch.getButton('A'):
            finch.print(message2)
            time.sleep(2)
            break
        time.sleep(0.1)


#Runs the Main Function
#Nothing should be below this line
if __name__ == "__main__":
    main()
