  MOV A, 1
  MOV B, 0
  PRINT B

.loop2:
  PRINT A
  MOV C, A
  ADD A, B
  MOV B, C
  JMP .loop2
