# Microcode

Microcode.txt contains the microcode for the CPU's implemented instruction set

## Micro From Instructions
Load data to the central bus. Only one from instruction should be activated per micro instruction.



```
fromRegisters   ;loads contents of selected register onto bus
fromALU         ;puts ALU output onto bus
fromIP          ;loads contents of intruction pointer onto bus
fromRAM         ;loads contents of RAM at IP address onto bus
fromRamAddr     ;makes ram output data at address contained inside the ramPointerRegister. "fromRAM" must also be on to output to bus.
```

## Conditional instructions

there are multiple variants of the ``if()`` instruction. the if instruction causes the CPU to compare a flag in the processor and jump if the flag is false. Only one ``if()`` instruction should be activated per micro instruction.

```
if(zero)
if(carry)
```
## Conditional modifiers
```
NOT            ;inverts the output of a flag comparison
```

## ALU mode instructions
the ALU has multiple modes of operation. only one ALU mode instruction should be activated per micro instruction.
```
ALU=ADD
ALU=SUB
ALU=NOT_B
ALU=AND
ALU=NAND
ALU=XOR
ALU=XNOR
ALU=SHR_B
ALU=B+1
ALU=B-1
ALU=OR
ALU=NOR
```
