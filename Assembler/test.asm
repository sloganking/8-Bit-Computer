counting:
      MOV A, 0

.countLoop:
    PRINT A
    INC A
    CMP A, 11
    JNC .countLoop

doubling:
  MOV A, 1
  
.doublingLoop:
  PRINT A
  SHL A
  JNC .doublingLoop
  
fib:
  MOV A, 1
  MOV B, 0
  PRINT B

.fibLoop:
  PRINT A
  MOV C, A
  ADD A, B
  MOV B, C
  JNC .fibLoop
  HLT
