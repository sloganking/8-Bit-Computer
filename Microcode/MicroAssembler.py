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


with open(f"./Microcode.txt") as input:
    with open(f"./Output/instrucToBinary.json", "w") as output:
        content = input.readlines()\


        # Start JSON object
        print(f"{{", file=output)
        # print(content)
        microAddress = 0
        for x in range(0, len(content)):
            tokens = str.split(content[x])
            strToPrint = ""

            if len(tokens) > 0:
                # if first char of string is ";", ignore line
                if tokens[0][0] == ";":
                    print("test")
                # if last char of first token is ":", instruction detected
                elif tokens[0][len(tokens[0]) - 1] == ":":
                    print("is :")

        # End JSON object
        print(f"}}", file=output)
