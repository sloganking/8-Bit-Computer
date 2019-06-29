  MOV A, 128
  
.halvingLoop:
  PRINT A
  SHR A
  JNZ .halvingLoop
  HLT