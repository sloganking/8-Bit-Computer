import json
import os
from os import listdir
from os.path import isfile, join
import time

class disassembler:

    def __init__(self):
        pass

    # takes machineCode bytes and returns a string of assembly
    def bytesToInstruc(self, bytes: list):
        params = self.binaryToInstrucLayout(bytes[0])
        tokenedParams = params.split("_")

        instructionString = ""
        instructionString = instructionString + \
            self.nameOfInstuc(self.binaryToInstrucLayout(bytes[0]))

        # x can be 1 and 2
        for x in range(1, 3):
            operand = ""
            if len(tokenedParams) > x:
                operandIsAddress = False
                if tokenedParams[x].startswith('[') and tokenedParams[x].endswith(']'):
                    operandIsAddress = True
                if x == 2:
                    instructionString = instructionString + ","

                if params in self.firstOperandShouldBeLabel and x == 1:
                    operand = self.getLabelFor(bytes[x])
                    if operandIsAddress:
                        operand = "[" + operand + "]"
                    instructionString = instructionString + " " + operand

                elif params in self.secondOperandShouldBeLabel and x == 2:
                    operand = self.getLabelFor(bytes[x])
                    if operandIsAddress:
                        operand = "[" + operand + "]"
                    instructionString = instructionString + " " + operand

                elif "reg" in tokenedParams[x]:
                    if self.binaryIsReg(bytes[x]):
                        operand = tokenedParams[x]
                        operand = operand.replace(
                            "reg", self.binaryToReg(bytes[x]))
                        if operandIsAddress:
                            operand = "[" + operand + "]"
                        instructionString = instructionString + " " + operand
                elif "const" in tokenedParams[x]:
                    operand = tokenedParams[x]
                    operand = operand.replace("const", str(bytes[x]))
                    if operandIsAddress:
                        operand = "[" + operand + "]"
                    instructionString = instructionString + " " + operand

        return instructionString

    def getLabelFor(self, number: int):

        # existing label
        if number in self.labelValues:
            return "l" + str(self.labels[self.labelValues.index(number)])
        # label does not exist
        else:
            self.labels.append(len(self.labels))
            self.labelValues.append(number)
            return "l" + str(len(self.labels) - 1)

    def binaryToReg(self, binary: int):
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

    def binaryIsReg(self, binary: int):
        try:
            self.binaryToReg(binary)
            return True
        except:
            return False

    # returns string of instruction's name with it's paramater(s) types

    def binaryToInstrucLayout(self, binary: int):
        binary = str(binary)
        return self.instrucNames[self.instrucNumbers.index(binary)]

    def nameOfInstuc(self, instruc: str):
        tokens = instruc.split("_")
        return tokens[0]

    def disassemble(self, inputBytes):
        self.linesToReturn = []

        # initialize known label number
        self.labels = []
        self.labelValues = []

        self.firstOperandShouldBeLabel = ["JMP_const",
                                          "JNC_const", "JC_const", "JNZ_const", "JZ_const"]

        self.secondOperandShouldBeLabel = ["MOV_reg_[const]"]

        # create byteArray with all file bytes
        byte = inputBytes

        # create and load binaryToIncruc array
        with open(f"./instrucToBinary.json") as json_data:
            instrucDict = json.load(json_data)

        self.instrucNames = list(instrucDict.keys())

        self.instrucNumbers = []
        for instrucName in self.instrucNames:
            self.instrucNumbers.append(instrucDict[instrucName])
        instructionBundles = []
        i = 0
        while(i < len(byte)):
            instrucLayout = self.binaryToInstrucLayout(byte[i])
            layoutTokens = instrucLayout.split("_")

            instructionBundle = []
            for x in range(len(layoutTokens)):
                instructionBundle.append(byte[i + x])

            instructionBundles.append(
                self.bytesToInstruc(instructionBundle))

            # sets i to location of next instruction.
            i = i + len(layoutTokens)

        i = 0
        for x in range(len(instructionBundles)):

            if i in self.labelValues:
                self.linesToReturn.append(self.getLabelFor(i) + ":" + "\n")

            self.linesToReturn.append("\t" + instructionBundles[x] + "\n")

            # keep track of what bytes we're on
            bundleTokens = instructionBundles[x].split(" ")
            i = i + len(bundleTokens)

        return self.linesToReturn
