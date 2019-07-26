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


def bytesToInstruc():
    pass


# def getListOfLabels():
#     with open(f"./test.asm") as labelInput:
#         listOfLabels = []
#         labelContent = labelInput.readlines()
#         for lx in range(0, len(labelContent)):
#             labelTokens = str.split(labelContent[lx])
#             if len(labelTokens) > 0:
#                 if str(labelTokens[0][-1:]) == ":":
#                     listOfLabels.append(labelTokens[0].replace(":", ""))
#         return listOfLabels


# def getLabelNumbers():
    # pass


# def isALabel(string):
#     if string in listOfLabels:
#         return True
#     else:
#         return False


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
