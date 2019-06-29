# Imports
# ===========================================================================


import os
from os import listdir
from os.path import isfile, join
import time


# Function declarations
# ===========================================================================


# Initialization
# ===========================================================================


# Start of main program
# ===========================================================================


f = open("./Output/microcode.bin", "rb")
try:
    bytes = f.read(4)
    while bytes != b'':
        # Do stuff with byte.
        print(bytes)
        print(len(bytes))
        # print(hex(int.from_bytes(bytes, "big")))
        bytes = f.read(4)

finally:
    f.close()
