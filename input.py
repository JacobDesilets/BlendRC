from enum import Enum
from queue import Queue


class Input():
    def __init__(self, arg):  # Expects a string as argument in the form "COMMAND P1 ..."
        self.arg = arg
        self.valid = True
        valid_commands = ['MOVE', 'ROTATE']
        self.input = self.arg.split(' ')
        if not self.input[0] in valid_commands:
            self.valid = False

        self.params = self.input[:1]


input_queue = Queue()
    