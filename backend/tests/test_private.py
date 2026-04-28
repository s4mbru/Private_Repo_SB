from private import classifyWeather, getValidInput, getWeather, reportWeather, weatherLights

#Class to instantiate a Finch dummy for test functions to test verification
class DummyFinch:
    def __init__(self, temperature = 0):
        self.temperature = temperature
        self.beak = None
        self.tail = None
        self.printed_messages = []

    def getTemperature(self):
        return self.temperature

    def setBeak(self, r, g, b):
        self.beak = (r, g, b)

    def setTail(self, port, r, g, b):
        self.tail = (port, r, g, b)

    def print(self, message):
        self.printed_messages.append(message)

    def setDisplay(self, display):
        self.display = display

#Testing weather functions for functional requirement
#-----------------------------------------------------

#Makes sure get method for weather functions work
def test_getWeatherTemperature():
    finch = DummyFinch(temperature=12)
    assert getWeather(finch) == 12

#Checks to see if cold condition is correct
def test_classifyColdWeather():
    assert classifyWeather(-1) == "cold"

#Checks to see if warm condition is correct
def test_classifyWarmWeather():
    assert classifyWeather(15) == "warm"

#Checks to see if hot condition is correct
def test_classifyHotWeather():
    assert classifyWeather(16) == "hot"

#Checks to see if cold condition lights are set correctly
def test_weatherColdLights():
    finch = DummyFinch()
    weatherLights(finch, "cold")
    assert finch.beak == (0, 0, 100)
    assert finch.tail == ("all", 0, 0, 100)

#Checks to see if warm condition lights are set correctly
def test_weatherWarmLights():
    finch = DummyFinch()
    weatherLights(finch, "warm")
    assert finch.beak == (0, 100, 0)
    assert finch.tail == ("all", 0, 100, 0)

#Checks to see if hot condition lights are set correctly
def test_weatherHotLights():
    finch = DummyFinch()
    weatherLights(finch, "hot")
    assert finch.beak == (100, 0, 0)
    assert finch.tail == ("all", 100, 0, 0)

#Simple check to see if temperature displays correctly
def test_reportWeatherMessage():
    finch = DummyFinch(temperature=-2)
    off = 0
    reportWeather(finch, off)
    assert finch.printed_messages == ["cold -2C"]
    assert finch.beak == (off, off, off)
    assert finch.tail == ("all", off, off, off)

#Testing user input for nonfunctional requirement
#-------------------------------------------------

#Tests to make sure space issue is eliminated(after)
def test_inputAfterSpace():
    assert getValidInput("6 ") == "6"

#Tests to make sure space issue is eliminated(before)
def test_inputBeforeSpace():
    assert getValidInput(" 7") == "7"

#Tests to make sure number in string issue is eliminated
def test_inputNumbersAndLetters():
    assert getValidInput("6f5") == "6"

#Tests to make sure invalid input feature works
def test_inputInvalid():
    assert getValidInput("abc") is None
