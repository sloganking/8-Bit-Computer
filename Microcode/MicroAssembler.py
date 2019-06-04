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


def thereIsAnotherInsturction():
    x2 = x + 1
    while x2 < len(content):

        tokens2 = str.split(content[x2])
        if len(tokens2) > 0:
            if tokens2[0][len(tokens2[0]) - 1] == ":":
                return True
        x2 = x2 + 1
    return False


# Start of main program
# ===========================================================================

removeAllFilesInDirectory("./Output/")


with open(f"./Microcode.txt") as input:
    with open(f"./Output/instrucToBinary.json", "w") as output:
        content = input.readlines()

        # Start JSON object
        print(f"{{", file=output)
        # print(content)
        microAddress = 0
        for x in range(0, len(content)):
            tokens = str.split(content[x])
            strToPrint = ""

            if len(tokens) > 0:
                # if first char of string is ";", ignore line
                if tokens[0][0] != ";":

                    # if last char of first token is ":", instruction detected
                    if tokens[0][len(tokens[0]) - 1] == ":":
                        strToPrint = "\t\"" + \
                            tokens[0][:-1] + "\":" + f"\"{microAddress}\""
                        if thereIsAnotherInsturction():
                            strToPrint = strToPrint + ","
                    # assemble micro instruction
                    else:
                        microAddress += 1   # keeps track of addresses for instrucToBinary.json

            # If something to print
            if strToPrint != "":
                strToPrint = f"{strToPrint}"
                print(f"{strToPrint}", file=output)

        # End JSON object
        print(f"}}", file=output)
