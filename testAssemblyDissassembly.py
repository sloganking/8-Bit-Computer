
from Disassembler.disassembler import disassembler
from Assembler.assembler import assembler

import numpy
import unittest


class testAssembler(unittest.TestCase):

    def test_assembler(self):

        myAssembler = assembler()
        myDisassembler = disassembler()

        with open("./test/test.asm", "r") as sourceAssemblyCode:
            codeLines = sourceAssemblyCode.readlines()

        machineCode1 = myAssembler.assemble(codeLines)

        reAssembled1 = myDisassembler.disassemble(machineCode1)

        machineCode2 = myAssembler.assemble(reAssembled1)

        numpy.testing.assert_array_equal(
            machineCode1, machineCode2, "Assembled code is not the same after disassembly and reassembly")

if __name__ == '__main__':
    unittest.main()