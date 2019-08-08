
from Disassembler.disassembler import disassembler
from Assembler.assembler import assembler

import numpy
import unittest


class testAssembler(unittest.TestCase):

    def test_assembler(self):

        myAssembler = assembler()
        myDisassembler = disassembler()

        # myAssembler.assemble("./test/test.asm",
        #                      "./test/machineCode.bin")

        # myDisassembler.disassemble(
        #     "./test/machineCode.bin", "./test/test2.asm")

        # myAssembler.assemble("./test/test2.asm",
        #                      "./test/machineCode2.bin")

        # with open("./test/machineCode.bin", "rb") as f:
        #     machineCode1 = f.read()

        # with open("./test/machineCode2.bin", "rb") as f:
        #     machineCode2 = f.read()

        # print("Byte1: ", machineCode1)
        # print("Byte2: ", machineCode2)

        # numpy.testing.assert_array_equal(
        #     machineCode1, machineCode2, "Assembled code is not the same after disassembly and reassembly")


        with open("./test/test.asm", "r") as assemblyCode:
            codeLines = assemblyCode.readlines()

        machineCode = myAssembler.assemble(codeLines)
        print(machineCode)

if __name__ == '__main__':
    unittest.main()