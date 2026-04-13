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
        self.printed_messages.append(message)

def test_startup_display_pattern():
    finch = FakeFinch()
    startupDisplay(finch)

    assert finch.display == [
        0, 1, 0, 1, 0,
        0, 1, 0, 1, 0,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        0, 1, 1, 1, 0
    ]

def test_end_display_pattern():
    finch = FakeFinch()
    endDisplay(finch)

    assert finch.display == [
        1, 1, 0, 1, 1,
        0, 0, 0, 0, 0,
        1, 0, 0, 0, 1,
        1, 0, 0, 0, 1,
        0, 1, 1, 1, 0
    ]

def test_when_done_button_a_shows_beautiful():
    finch = FakeFinch(button_a=True, button_b=False)
    whenDone(finch)

    assert "BEAUTIFUL!" in finch.printed_messages

def test_when_done_button_b_shows_amazing():
    finch = FakeFinch(button_a=False, button_b=True)
    whenDone(finch)

    assert "AMAZING!!" in finch.printed_messages

def test_when_done_both_buttons_show_both_messages():
    finch = FakeFinch(button_a=True, button_b=True)
    whenDone(finch)

    assert "BEAUTIFUL!" in finch.printed_messages
    assert "AMAZING!!" in finch.printed_messages

def test_when_done_no_button_shows_no_message():
    finch = FakeFinch(button_a=False, button_b=False)
    whenDone(finch)

    assert finch.printed_messages == []
