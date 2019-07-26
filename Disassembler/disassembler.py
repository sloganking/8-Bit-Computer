# Imports
# ===========================================================================

import json
import os
from os import listdir
from os.path import isfile, join
import time

# Function declarations
# ===========================================================================


def removeAllFilesInDirectory(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    for i in range(0, len(onlyfiles)):
        os.remove(f"{directory}{onlyfiles[i]}")


# takes machineCode bytes and returns a string of assembly
def bytesToInstruc(bytes: []):
    params = binaryToInstrucLayout(bytes[0])
    tokenedParams = params.split("_")

    instructionString = ""
    instructionString = nameOfInstuc(binaryToInstrucLayout(bytes[0]))

    operand = ""
    if len(tokenedParams) > 1:
        if "reg" in tokenedParams[1]:
            if binaryIsReg(bytes[1]):
                operand = tokenedParams[1]
                operand = operand.replace("reg", binaryToReg(bytes[1]))
                instructionString = instructionString + " " + operand
        if "const" in tokenedParams[1]:
            operand = tokenedParams[1]
            operand = operand.replace("const", bytes[1])
            instructionString = instructionString + " " + operand

    return instructionString


def binaryToReg(binary: int):
    if binary == 0:
        return "A"
    elif binary == 1:
        return "B"
    elif binary == 2:
        return "C"
    elif binary == 3:
        return "D"
    else:
        assert (False), f"No reg for given binary: {binary}"


def binaryIsReg(binary: int):
    try:
        binaryToReg(binary)
        return True
    except:
        return False


# returns string of instruction's name with it's paramater(s) types
def binaryToInstrucLayout(binary: int):
    binary = str(binary)
    return instrucNames[instrucNumbers.index(binary)]


def nameOfInstuc(instruc: str):
    tokens = instruc.split("_")
    return tokens[0]

# Initialization
# ===========================================================================


removeAllFilesInDirectory("./Output/")

# create byteArray with all file bytes
with open("./machineCode.bin", "rb") as f:
    byte = f.read()


# create and load binaryToIncruc array
with open(f"./instrucToBinary.json") as json_data:
    instrucDict = json.load(json_data)
    # print(instrucToBinary[0])

instrucNames = list(instrucDict.keys())

instrucNumbers = []
for instrucName in instrucNames:
    instrucNumbers.append(instrucDict[instrucName])

# Start of main program
# ===========================================================================
