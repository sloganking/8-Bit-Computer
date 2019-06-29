# Assembler

assembler.py takes the assembly program located in test.asm turns it into executable machine code located in Output/machineCode.bin.

instrucToBinary.json contains a list of all valid instructions and is used by assembler.py for the assembling process.

## Instruction format

Every instruction has two parts, the instruction and it's operands. instruction can take between zero and two operands.

Operands can be a constant (an unsigned integer between 0 and 255), register (notated by letters), or memory address (specified by having a constant or register encased in brackets like so ``[A] or [5]``)


For instructions with two operands, the first (lefthand) operand is the destination operand, and the second (righthand) operand is the source. That is (destination<-source)

So the instruction ``ADD A, B`` will add the contents inside the ``A`` and ``B`` registers, and store the result in the ``A`` Register.


## Instruction machine code

Seeing as this is an 8 bit computer, all instructions and operands are represented with one byte. This means one instruction which contains two operands, such as ``MOV A, 5`` will consist of three bytes ``x03 x00 x05``. ``x03`` representing the ``MOV_reg_const`` instruction, ``x00`` representing the A register and ``x05`` representing the constant "5".
