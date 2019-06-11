# Imports
# ===========================================================================

import json
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
    regCharacters = ["A", "B", "C", "D"]
    isAddress = False
    if token.startswith('[') and token.endswith(']'):
        isAddress = True
        token = token.replace("[", "")
        token = token.replace("]", "")

    if "," in token:
        token = token.replace(",", "")
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
    elif isALabel(token):
        if isAddress:
            return "[const]"
        else:
            return "const"


def tokensToInstruc(tokens):
    instruc = ""
    if len(tokens) > 0:
        instruc = instruc + tokens[0]
    if len(tokens) > 1:
        instruc = instruc + "_" + returnType(tokens[1])
    if len(tokens) > 2:
        instruc = instruc + "_" + returnType(tokens[2])
    return instruc


def getListOfLabels():
    with open(f"./test.asm") as labelInput:
        listOfLabels = []
        labelContent = labelInput.readlines()
        for lx in range(0, len(labelContent)):
            labelTokens = str.split(labelContent[lx])
            if len(labelTokens) > 0:
                if str(labelTokens[0][-1:]) == ":":
                    listOfLabels.append(labelTokens[0].replace(":", ""))
        return listOfLabels


def getLabelNumbers():
    labelNumbers = []
    with open(f"./test.asm") as labelInput:
        currentByte = 0
        labelContent = labelInput.readlines()
        for lx in range(0, len(labelContent)):

            labelTokens = str.split(labelContent[lx])
            if len(labelTokens) > 0:
                if str(labelTokens[0][-1:]) == ":":
                    labelNumbers.append(currentByte)
                elif instrucToBinary(tokensToInstruc(labelTokens)):
                    currentByte += len(labelTokens)
    return labelNumbers


def isALabel(string):
    if string in listOfLabels:
        return True
    else:
        return False


def instrucToBinary(string):
    with open(f"./instrucToBinary.json") as json_data:
        instrucToBinary = json.load(json_data)
        try:
            return instrucToBinary[string]
        except:
            return False


def regToBinary(reg):
    reg = reg.replace(",", "")
    if reg == "A":
        return 0
    elif reg == "B":
        return 1
    elif reg == "C":
        return 2
    elif reg == "D":
        return 3


def constToBinary(const):
    if isALabel(const):
        return labelNumbers[listOfLabels.index(const)]
    else:
        return int(const.replace(",", ""))

    # Start of main program
    # ===========================================================================


removeAllFilesInDirectory("./Output/")

with open(f"./test.asm") as input:
    with open(f"./Output/machineCode.bin", "w") as output:
        content = input.readlines()
        listOfLabels = getListOfLabels()
        labelNumbers = getLabelNumbers()
        machineCodeBytes = bytearray()

        for x in range(0, len(content)):
            tokens = str.split(content[x])
            instruc = tokensToInstruc(tokens)
            instructionBytes = []

            # print("tokens:      " + str(tokens))
            # print(instruc)
            # print("isAnInstruction:     " + str(instrucToBinary(instruc)))
            # print(machineCodeBytes)
            # print()

            if instrucToBinary(tokensToInstruc(tokens)):
                # print(f"{instrucToBinary(tokensToInstruc(tokens))}", file=output)
                machineCodeBytes.append(
                    int(instrucToBinary(tokensToInstruc(tokens))))
                # if len(tokens) > 1:
                #     if tokensToInstruc(tokens)
                #     print(f"{}", file=output)

        print(machineCodeBytes)
        print(f"{machineCodeBytes}", file=output)

        print("Byte[0]:     " + str(machineCodeBytes[2]))

        print("{0:b}".format(machineCodeBytes[2]))
