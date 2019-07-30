from Disassembler.disassembler import disassembler
from Assembler.assembler import assembler


myDisassembler = disassembler()
myDisassembler.disassemble(
    "./Disassembler/machineCode.bin", "./Disassembler/Output/test.asm")


myAssembler = assembler()
myAssembler.assemble("./Assembler/test.asm",
                     "./Assembler/Output/machineCode.bin")
