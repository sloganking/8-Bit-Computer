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
