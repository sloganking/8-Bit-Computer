# Imports
# ===========================================================================

import os
from os import listdir
from os.path import isfile, join
import time

# Function declarations
# ===========================================================================

# Remove all files in given directory
def removeAllFilesInDirectory(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    for i in range(0, len(onlyfiles)):
        os.remove(f"{directory}{onlyfiles[i]}")

# Start of main program
# ===========================================================================

removeAllFilesInDirectory("./Output/")

with open(f"./instrucToBinary.json") as input:
    with open(f"./Output/machineCode.json", "w") as output:
        content = input.readlines()

        testInt = 100
        print(isinstance(testInt, int))

         # Start JSON object
        print(f"{{", file=output)

        # End JSON object
        print(f"}}", file=output)