  MOV A, 128
  
.halfingLoop:
  PRINT A
  SHR A
  JNZ .halfingLoop
  HLT