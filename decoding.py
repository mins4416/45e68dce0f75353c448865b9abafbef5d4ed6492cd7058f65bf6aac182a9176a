from immlib import *

def get_cnt(buf_read):
	len = 1
	for x in buf_read:
		if x != "\x00":
			len = len + 1
		else:
			return len
	return len
	
def main(args):
	imm = Debugger()
	current_EIP_addr = imm.getRegs()['EIP']
	current_EAX_addr = imm.getRegs()['EAX']
	buf_addr = 0x41C5B8
	last_addr = 0x40590A
	while(current_EIP_addr != last_addr):
		buf_temp = 'nop'
		buf_read = 'pon'
		if current_EAX_addr == 0x41C5B8:
			if buf_temp == buf_read:
				pass
			else:
				buf_read = imm.readMemory(buf_addr, 0x20)
				len = get_cnt(buf_read)
				buf_read = imm.readMemory(buf_addr, len)
				buf_file = open("c:\\temp\\buf.txt", "a")
				buf_file.write(buf_read+"\n")
				buf_file.close()
				buf_temp = buf_read
		current_EIP_addr = imm.getRegs()['EIP']
		current_EAX_addr = imm.getRegs()['EAX']
		imm.stepOver()
	#imm.log(str(buf_read))
	'''
	while(current_addr != 0x40590A):
		eip_addr = imm.getRegs()['EIP']
		opcode = imm.disasm(eip_addr)
		instr = opcode.getDisasm()
		if (instr == "CALL a.004012B0"):
			imm.stepOver()
	'''
	return "[*] Pycommand Executed!"