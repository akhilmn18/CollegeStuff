	LXI H,7050
	LXI D,7060
	MOV B,M
	INX H
	INX H
	MOV A,M
	ADC B
	STAX D
	INX D
	INX H
	MOV A,M
	DCX H
	DCX H
	MOV B,M
	ADC B
	STAX D
	INX D
	MVI A,00
	ADC A
	STAX D
	HLT

# org 7050h
# db 91,98,02,91
	
	
			