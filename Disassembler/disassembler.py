# Imports
# ===========================================================================

import json
import os
from os import listdir
from os.path import isfile, join
import time

# Function declarations
# ===========================================================================


def removeAllFilesInDirectory(directory: str):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    for i in range(0, len(onlyfiles)):
        os.remove(f"{directory}{onlyfiles[i]}")


# takes machineCode bytes and returns a string of assembly
def bytesToInstruc(bytes: list):
    params = binaryToInstrucLayout(bytes[0])
    tokenedParams = params.split("_")

    instructionString = ""
    instructionString = instructionString + \
        nameOfInstuc(binaryToInstrucLayout(bytes[0]))

    # x can be 1 and 2
    for x in range(1, 3):
        operand = ""
        if len(tokenedParams) > x:
            if x == 2:
                instructionString = instructionString + ","

            if params in firstOperandShouldBeLabel and x == 1:
                operand = getLabelFor(bytes[x])
                instructionString = instructionString + " " + operand

            elif "reg" in tokenedParams[x]:
                if binaryIsReg(bytes[x]):
                    operand = tokenedParams[x]
                    operand = operand.replace("reg", binaryToReg(bytes[x]))
                    instructionString = instructionString + " " + operand
            elif "const" in tokenedParams[x]:
                operand = tokenedParams[x]
                operand = operand.replace("const", str(bytes[x]))
                instructionString = instructionString + " " + operand

    return instructionString


def getLabelFor(number: int):

    # existing label
    if number in labelValues:
        return "l" + str(labels[labelValues.index(number)])
    # label does not exist
    else:
        labels.append(len(labels))
        labelValues.append(number)
        return "l" + str(len(labels) - 1)


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

# initialize known label number

labels = []
labelValues = []

firstOperandShouldBeLabel = ["JMP_const",
                             "JNC_const", "JC_const", "JNZ_const", "JZ_const"]

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

# print(bytesToInstruc([3, 0, 1]))

with open(f"./Output/test.asm", "w") as output:
    instructionBundles = []
    i = 0
    while(i < len(byte)):
        instrucLayout = binaryToInstrucLayout(byte[i])
        layoutTokens = instrucLayout.split("_")

        instructionBundle = []
        for x in range(len(layoutTokens)):
            instructionBundle.append(byte[i + x])

        # write assembly line to output file
        # output.write(bytesToInstruc(instructionBundle) + "\n")
        instructionBundles.append(bytesToInstruc(instructionBundle))

        # sets i to location of next instruction.
        i = i + len(layoutTokens)

    i = 0
    for x in range(len(instructionBundles)):

        if i in labelValues:
            output.write(getLabelFor(i) + ":" + "\n")

        output.write("\t" + instructionBundles[x] + "\n")

        # keep track of what bytes we're on
        bundleTokens = instructionBundles[x].split(" ")
        i = i + len(bundleTokens)
