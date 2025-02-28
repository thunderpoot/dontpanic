import sys

# Default message
_message = ''

def set_message(msg: str):
    """Set a custom message for when ^C is pressed"""
    global _message
    _message = msg

def ignore_keyboard_interrupt(exc_type, exc_value, traceback):
    """Handles KeyboardInterrupt"""
    if exc_type is KeyboardInterrupt:
        print(_message)
    else:
        sys.__excepthook__(exc_type, exc_value, traceback)

sys.excepthook = ignore_keyboard_interrupt
