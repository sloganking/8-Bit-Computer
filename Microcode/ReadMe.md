# Microcode

Microcode.txt contains the microcode for the CPU's implemented instruction set

## From Instructions
Load data to the central bus. Only one from instruction should be activated per micro instruction.
```
fromRegisters   ;loads contents of selected register onto bus
fromALU         ;puts ALU output onto bus
fromIP          ;loads contents of intruction pointer onto bus
fromRAM         ;loads contents of RAM at IP address onto bus
fromRamAddr     ;makes ram output data at address contained inside the ramPointerRegister. "fromRAM" must also be on to output to bus.
```

## To instructions
save data from central bus to specified register.
```
toNumDisplay      ; seven segment display used to display 8 bit unsigned numbers to the user
toALU_A
toALU_B
toWriteReg        ; saves contents from bus to register specified by the regWrite register
toRegWrite        ; determins which register will be written to
toRegRead         ; determines which register will be read from
toRamRead         ; used to grab data from a specific ram address
toInstrucDecoder
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

## Other

```
incIP       ; increments the instruction pointer "fromRAM" always returns data from the address inside the instruction pointer unless "fromRamAddr" is on
endMP       ; ends Micro Program
