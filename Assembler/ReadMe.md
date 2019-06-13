# Assembler

assembler.py takes the assembly program located in test.asm turns it into executable machine code located in Output/machineCode.bin file.

instrucToBinary.json contains a list of all valid instructions and is used by assembler.py for the assembling process.

## Instruction format

Every instruction has two parts, the operation and it's arguments. Operations can take between one and two arguments.

## Instruction machine code

Seeing as this is an 8 bit computer, all instructions and arguments are represented with one byte. This means one instruction which contains two arguments, such as ``MOV A, 5`` will consist of three bytes ``x03 x00 x05``. ``x03`` representing the ``MOV_reg_const`` instruction, ``x00`` representing the A register and ``x05`` representing the constant "5".
