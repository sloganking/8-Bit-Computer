import json
import os
from os import listdir
from os.path import isfile, join
import time


class assembler:

    def __init__(self):
        # registers in ISA.
        # index in array == machineCode
        self.regs = ["A", "B", "C", "D"]

    def __RepresentsInt(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def __returnType(self, token):
        isAddress = False
        if token.startswith('[') and token.endswith(']'):
            isAddress = True
            token = token.replace("[", "")
            token = token.replace("]", "")

        if "," in token:
            token = token.replace(",", "")
        if self.__RepresentsInt(token):
            if isAddress:
                return "[const]"
            else:
                return "const"
        elif len(token) == 1 and token in self.regs:
            if isAddress:
                return "[reg]"
            else:
                return "reg"
        elif self.__isALabel(token):
            if isAddress:
                return "[const]"
            else:
                return "const"

    def __tokensToInstruc(self, tokens):
        instruc = ""
        if len(tokens) > 0:
            instruc = instruc + tokens[0]
        if len(tokens) > 1:
            instruc = instruc + "_" + self.__returnType(tokens[1])
        if len(tokens) > 2:
            instruc = instruc + "_" + self.__returnType(tokens[2])
        return instruc

    def __getListOfLabels(self):
        self.listOfLabels = []
        labelContent = self.linesToAssemble
        for lx in range(0, len(labelContent)):
            labelTokens = str.split(labelContent[lx])
            if len(labelTokens) > 0:
                if str(labelTokens[0][-1:]) == ":":
                    self.listOfLabels.append(
                        labelTokens[0].replace(":", ""))
        return self.listOfLabels

    def __getLabelNumbers(self):
        self.labelNumbers = []
        currentByte = 0
        labelContent = self.linesToAssemble
        for lx in range(0, len(labelContent)):

            labelTokens = str.split(labelContent[lx])
            if len(labelTokens) > 0:
                if str(labelTokens[0][-1:]) == ":":
                    self.labelNumbers.append(currentByte)
                elif self.__instrucToBinary(self.__tokensToInstruc(labelTokens)):
                    currentByte += len(labelTokens)
        return self.labelNumbers

    def __isALabel(self, string):
        if string in self.listOfLabels:
            return True
        else:
            return False

    def __instrucToBinary(self, string):
        with open(f"./instrucToBinary.json") as json_data:
            binInstruc = json.load(json_data)
            try:
                return binInstruc[string]
            except:
                return False

    def __regToBinary(self, reg):
        try:
            return self.regs.index(reg)
        except:
            return False

    def __constToBinary(self, const):
        if const.startswith('[') and const.endswith(']'):
            const = const.replace("[", "")
            const = const.replace("]", "")
        if self.__isALabel(const):
            return self.labelNumbers[self.listOfLabels.index(const)]
        else:
            return int(const.replace(",", ""))

    """
    takes list of file lines and returns a bytearray of corresponding machine code
    """
    def assemble(self, linesToAssemble):

        self.linesToAssemble = linesToAssemble
        self.content = linesToAssemble
        self.listOfLabels = self.__getListOfLabels()
        self.labelNumbers = self.__getLabelNumbers()
        self.machineCodeBytes = bytearray()

        for x in range(0, len(self.content)):
            tokens = str.split(self.content[x])
            instruc = self.__tokensToInstruc(tokens)
            instructionBytes = []

            # if "tokens" represnt a valid instruction
            if self.__instrucToBinary(self.__tokensToInstruc(tokens)):
                self.machineCodeBytes.append(
                    int(self.__instrucToBinary(self.__tokensToInstruc(tokens))))
                for x1 in range(1,3):
                    if len(tokens) > x1:
                        if "reg" in self.__returnType(tokens[x1]):
                            self.machineCodeBytes.append(
                                self.__regToBinary(tokens[x1]))
                        elif "const" in self.__returnType(tokens[x1]):
                            self.machineCodeBytes.append(
                                self.__constToBinary(tokens[x1]))

        return self.machineCodeBytes
