import sys
from intelhex import IntelHex
from util import assemble

def write_intel_hex(machine_code, output_file):
    """Writes assembled machine code to an Intel HEX file using the IntelHex package."""
    ih = IntelHex()
    address = 0  # Start at address 0

    for instruction in machine_code:
        bytes_ = instruction.to_bytes(3, byteorder="little")  # Convert 24-bit instruction to 3 bytes
        ih[address] = bytes_[0]
        ih[address + 1] = bytes_[1]
        ih[address + 2] = bytes_[2]
        address += 3  # Move to next instruction

    ih.write_hex_file(output_file)
    print(f"Assembly successful! Intel HEX output written to {output_file}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python assembler.py input.asm output.hex")
        return

    input_file, output_file = sys.argv[1], sys.argv[2]

    with open(input_file, "r") as f:
        source_code = f.read()

    machine_code = assemble(source_code)
    write_intel_hex(machine_code, output_file)

if __name__ == "__main__":
    main()
