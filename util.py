from mnemonics import mnemonics
from registers import registers


def assemble_line(line):
    parts = line.strip().split()
    if not parts or parts[0].startswith(";"):
        return
    
    mnemonic = parts[0].upper()
    opcode = mnemonics[mnemonic]

    if mnemonic == "NOP":
        return 0
    elif mnemonic == "MOV":
        rd, rs0 = parts[1], parts[2]
        if rd not in registers or rs0 not in registers:
            raise ValueError(f"Invalid registers: {rd}, {rs0}")
        return (registers[rs0] << 8) | (registers[rd] << 4) | opcode

    elif mnemonic == "LDI":
        rd, imm = parts[1], int(parts[2], 0)
        if rd not in registers:
            raise ValueError(f"Invalid register: {rd}")
        if not (0 <= imm <= 255):  # Ensure 8-bit immediate
            raise ValueError(f"Immediate out of range: {imm}")
        return (imm << 16) | (registers[rd] << 4) | opcode

    elif mnemonic == "LOAD":
        rd, rs0, rs1 = parts[1], parts[2], parts[3]
        imm = int(parts[4], 0) & 0xFF if len(parts) == 5 else 0x00  # Ensure 8-bit immediate
        if rd not in registers or rs0 not in registers or rs1 not in registers:
            raise ValueError(f"Invalid registers: {rd}, {rs0}, {rs1}")
        return (imm << 16) | (registers[rs1] << 12) | (registers[rs0] << 8) | (registers[rd] << 4) | opcode

    elif mnemonic == "STORE":
        rd, rs0, rs1 = parts[1], parts[2], parts[3]

        print("rd, rs0, rs1")
        print(f"{rd}, {rs0}, {rs1}")

        imm = int(parts[4], 0) if len(parts) == 5 else 0x00  # Ensure 8-bit immediate
        if rd not in registers or rs0 not in registers or rs1 not in registers:
            raise ValueError(f"Invalid registers: {rd}, {rs0}, {rs1}")
        print(f"{imm:02X}")
        return (imm << 16) | (registers[rs1] << 12) | (registers[rs0] << 8) | (registers[rd] << 4) | opcode


def assemble(code):
    binary = []
    for line in code.split("\n"):
        bnry = assemble_line(line)
        if bnry is not None:
            print(f"{line} : 0x{f'{bnry:06X}'[::-1]}")
            binary.append(bnry)
    return binary
