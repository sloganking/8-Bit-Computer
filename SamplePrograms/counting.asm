    MOV A, 0

.countLoop:
    PRINT A
    INC A
    CMP A, 11
    JNC .countLoop
    HLT
