	MOV A, 0
l0:
	PRINT A
	INC A
	CMP A, 11
	JNC l0
	MOV A, 1
l1:
	PRINT A
	SHL A
	JNC l1
	MOV A, 128
l2:
	PRINT A
	SHR A
	JNZ l2
	MOV A, 1
	MOV B, 0
	PRINT B
l3:
	PRINT A
	MOV C, A
	ADD A, B
	MOV B, C
	JNC l3
	HLT