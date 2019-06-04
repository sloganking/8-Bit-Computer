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

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def returnType(token):
    regCharacters = ["A","B","C","D"]
    isAddress = False
    if token.startswith('[') and token.endswith(']'):
        isAddress = True
        token = token.replace("[", "")
        token = token.replace("]", "")
    # print("token:   " + token)
    if RepresentsInt(token):
        if isAddress:
            return "[const]"
        else: 
            return "const"
    elif len(token) == 1 and token in regCharacters:
        if isAddress:
            return "[reg]"
        else:
            return "reg"

# Start of main program
# ===========================================================================

removeAllFilesInDirectory("./Output/")

with open(f"./instrucToBinary.json") as input:
    with open(f"./Output/machineCode.json", "w") as output:
        content = input.readlines()
        
        testToken = "[B]"
        returnType(testToken)

         # Start JSON object
        print(f"{{", file=output)

        # End JSON object
        print(f"}}", file=output)