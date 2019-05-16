  MOV A, 1
  
.doublingLoop:
  PRINT A
  SHL A
  JNC .doublingLoop
  HLT
