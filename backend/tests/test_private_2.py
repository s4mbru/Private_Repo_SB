from private import startupDisplay, endDisplay, whenDone
class FakeFinch:
        def __init__(self, button_a=False, button_b=False):
        self.display = None
        self.printed_messages = []
        self.button_a = button_a
        self.button_b = button_b

        def setDisplay(self, pattern):
                self.display = pattern

        def getButton(self, button_name):
                if button_name == 'A':
                        return self.button_a
        if button_name == 'B':
                return self.button_b
        return False

        def print(self, message):
                self.printed_messages.append(message)finch.playNote(64,0.5)# E4

def test_bad_num_input():
        finch = FakeFinch()
        num = "6 ";

        assert finch.setMove('F', speed, distance) #Finch moves forward

def test_mult_num_input():
        finch = FakeFinch()
        num = "6f5";

        assert finch.setMove('F', speed, distance) #Finch moves forward
