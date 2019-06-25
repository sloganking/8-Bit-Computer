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


def fullMicInstrucToBinary(tokens):
    microInstruc = 0

    for x in range(0, len(tokens)):
        tokens[x] = tokens[x].replace(",", "")
    for x in range(0, len(tokens)):
        try:
            microInstruc = microInstruc | micInstrucToBinary[tokens[x]]
        except:
            print("Error: ", tokens[x], " is not a valid instruction")
            return False
    return microInstruc


# Initialization
# ===========================================================================


micInstrucToBinary = {

    # From Instructions
    "fromReg":      0b00000000000000000000000000100000,
    "fromALU":      0b00000000000000000000000000010000,
    "fromIP":       0b00000000000000000000000000001000,
    "fromRAM":      0b00000000000000000000000000000100,
    "fromRamAddr":  0b00000000000000000000000000000010,

    # To instructions
    "toNumDisplay": 0b00000000000100000000000000000000,
    "toALU_A":      0b00000010000000000000000000000000,
    "toALU_B":      0b00000001000000000000000000000000,
    "toWriteReg":   0b00000000001000000000000000000000,
    "toRegWrite":   0b00000000010000000000000000000000,
    "toRegRead":    0b00000000100000000000000000000000,
    "toRamRead":    0b00000100000000000000000000000000,
    "toID":         0b01000000000000000000000000000000,

    # Conditional instructions
    "if(zero)":     0b00000000000000000000100000000000,
    "if(carry)":    0b00000000000000000000010000000000,
    "if(ujump)":    0b00000000000000000000111100000000,

    # Conditional modifiers
    "NOT":          0b00000000000000000000000010000000,

    # ALU mode instructions
    "ALU=ADD":      0b00000000000000001000000000000000,
    "ALU=SUB":      0b00000000000000000100000000000000,
    "ALU=NOT_B":    0b00000000000000001100000000000000,
    "ALU=AND":      0b00000000000000000010000000000000,
    "ALU=NAND":     0b00000000000000001010000000000000,
    "ALU=XOR":      0b00000000000000000110000000000000,
    "ALU=XNOR":     0b00000000000000001110000000000000,
    "ALU=SHR_B":    0b00000000000000000001000000000000,
    "ALU=INC_B":    0b00000000000000001001000000000000,
    "ALU=DEC_B":    0b00000000000000000101000000000000,
    "ALU=OR":       0b00000000000000001101000000000000,
    "ALU=NOR":      0b00000000000000000011000000000000,

    # Other
    "incIP":        0b00001000000000000000000000000000,
    "endMP":        0b10000000000000000000000000000000,
    "HLT":          0b00000000000000010000000000000000
}

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
                        print(tokens)
                        if fullMicInstrucToBinary(tokens):
                            print(bin(fullMicInstrucToBinary(tokens)))
                        else:
                            print(
                                "Error: invalid micro instruction given on line: ", x + 1)
                            break

            # If something to print
            if strToPrint != "":
                strToPrint = f"{strToPrint}"
                print(f"{strToPrint}", file=output)

        # End JSON object
        print(f"}}", file=output)
