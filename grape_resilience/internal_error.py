#!/usr/bin/env python3

# TODO: Create error codes
# ERROR_1 = 1
# ERROR_2 = 2
# ...

class InternalError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message

def print_error(error):
    pass
    # if error.code == ERROR_1:
        # pass
        # #print("There was an error ..." + error.message)
