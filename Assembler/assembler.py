# Imports
# ===========================================================================

import json
import os
from os import listdir
from os.path import isfile, join
import time

# Function declarations
# ===========================================================================


class assembler:

    def __init__(self):
        pass

    def removeAllFilesInDirectory(self, directory):
        onlyfiles = [f for f in listdir(
            directory) if isfile(join(directory, f))]
        for i in range(0, len(onlyfiles)):
            os.remove(f"{directory}{onlyfiles[i]}")

    def RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def returnType(self, token):
        regCharacters = ["A", "B", "C", "D"]
        isAddress = False
        if token.startswith('[') and token.endswith(']'):
            isAddress = True
            token = token.replace("[", "")
            token = token.replace("]", "")

        if "," in token:
            token = token.replace(",", "")
        # print("token:   " + token)
        if self.RepresentsInt(token):
            if isAddress:
                return "[const]"
            else:
                return "const"
        elif len(token) == 1 and token in regCharacters:
            if isAddress:
                return "[reg]"
            else:
                return "reg"
        elif self.isALabel(token):
            if isAddress:
                return "[const]"
            else:
                return "const"

    def tokensToInstruc(self, tokens):
        instruc = ""
        if len(tokens) > 0:
            instruc = instruc + tokens[0]
        if len(tokens) > 1:
            instruc = instruc + "_" + self.returnType(tokens[1])
        if len(tokens) > 2:
            instruc = instruc + "_" + self.returnType(tokens[2])
        return instruc

    def getListOfLabels(self):
        with open(self.inputDir) as labelInput:
            self.listOfLabels = []
            labelContent = labelInput.readlines()
            for lx in range(0, len(labelContent)):
                labelTokens = str.split(labelContent[lx])
                if len(labelTokens) > 0:
                    if str(labelTokens[0][-1:]) == ":":
                        self.listOfLabels.append(
                            labelTokens[0].replace(":", ""))
            return self.listOfLabels

    def getLabelNumbers(self):
        self.labelNumbers = []
        with open(self.inputDir) as labelInput:
            currentByte = 0
            labelContent = labelInput.readlines()
            for lx in range(0, len(labelContent)):

                labelTokens = str.split(labelContent[lx])
                if len(labelTokens) > 0:
                    if str(labelTokens[0][-1:]) == ":":
                        self.labelNumbers.append(currentByte)
                    elif self.instrucToBinary(self.tokensToInstruc(labelTokens)):
                        currentByte += len(labelTokens)
        return self.labelNumbers

    def isALabel(self, string):
        if string in self.listOfLabels:
            return True
        else:
            return False

    def instrucToBinary(self, string):
        with open(f"./instrucToBinary.json") as json_data:
            binInstruc = json.load(json_data)
            try:
                return binInstruc[string]
            except:
                return False

    def regToBinary(self, reg):
        reg = reg.replace(",", "")
        if reg == "A":
            return 0
        elif reg == "B":
            return 1
        elif reg == "C":
            return 2
        elif reg == "D":
            return 3
        else:
            return False

    def constToBinary(self, const):
        if self.isALabel(const):
            return self.labelNumbers[self.listOfLabels.index(const)]
        else:
            return int(const.replace(",", ""))

    # Initialization
    # ===========================================================================

    # removeAllFilesInDirectory("./Output/")

    def assemble(self, inputDir, outputDir):
        with open(outputDir, "wb") as output:
            with open(inputDir) as input:
                self.inputDir = inputDir
                self.content = input.readlines()
                self.listOfLabels = self.getListOfLabels()
                self.labelNumbers = self.getLabelNumbers()
                self.machineCodeBytes = bytearray()

                # Start of main program
                # ===========================================================================

                for x in range(0, len(self.content)):
                    tokens = str.split(self.content[x])
                    instruc = self.tokensToInstruc(tokens)
                    instructionBytes = []

                    # if "tokens" represnt a valid instruction
                    if self.instrucToBinary(self.tokensToInstruc(tokens)):
                        self.machineCodeBytes.append(
                            int(self.instrucToBinary(self.tokensToInstruc(tokens))))
                        if len(tokens) > 1:
                            if "reg" in self.returnType(tokens[1]):
                                self.machineCodeBytes.append(
                                    self.regToBinary(tokens[1]))
                            elif "const" in self.returnType(tokens[1]):
                                self.machineCodeBytes.append(
                                    self.constToBinary(tokens[1]))
                        if len(tokens) > 2:
                            if "reg" in self.returnType(tokens[2]):
                                self.machineCodeBytes.append(
                                    self.regToBinary(tokens[2]))
                            elif "const" in self.returnType(tokens[2]):
                                self.machineCodeBytes.append(
                                    self.constToBinary(tokens[2]))

                output.write(self.machineCodeBytes)
                print("Assembler finished")
                print("wrote " + str(len(self.machineCodeBytes)) +
                      " bytes to output")
                print(self.machineCodeBytes)
