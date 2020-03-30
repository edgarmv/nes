from enum import Enum
import sys


class AddressingMode(Enum):
    IMPLIED = 0
    IMMEDIATE = 1
    ABSOLUTE = 2
    ABSOLUTE_X = 3
    RELATIVE = 4


OPCODES = {
        0x10: {
            "mnemonic": "BPL ${:d}",
            "full_name": "Branch on PLus",
            "effect": "IF [N == 0]; Update PC",
            "addressing_mode": AddressingMode.RELATIVE,
            "num_bytes": 2,
        },
        0x20: {
            "mnemonic": "JSR ${:04X}",
            "full_name": "Jump to SubRoutine",
            "effect": "Stack = PC-1, Update PC",
            "addressing_mode": AddressingMode.ABSOLUTE,
            "num_bytes": 3,
        },
        0x78: {
            "mnemonic": "SEI",
            "full_name": "SEt Interrupt disable",
            "effect": "I = 1",
            "addressing_mode": AddressingMode.IMPLIED,
            "num_bytes": 1,
        },
        0x8D: {
            "mnemonic": "STA ${:04X}",
            "full_name": "STore Accumulator",
            "effect": "M = A",
            "addressing_mode": AddressingMode.ABSOLUTE,
            "num_bytes": 3,
        },
        0x9A: {
            "mnemonic": "TXS",
            "full_name": "Transfer X to Stack pointer",
            "effect": "S = X",
            "addressing_mode": AddressingMode.IMPLIED,
            "num_bytes": 1,
        },
        0xA0: {
            "mnemonic": "LDY #${:02X}",
            "full_name": "LoaD Y register",
            "effect": "Y,Z,N = M",
            "addressing_mode": AddressingMode.IMMEDIATE,
            "num_bytes": 2,
        },
        0xA2: {
            "mnemonic": "LDX #${:02X}",
            "full_name": "LoaD X register",
            "effect": "X,Z,N = M",
            "addressing_mode": AddressingMode.IMMEDIATE,
            "num_bytes": 2,
        },
        0xA9: {
            "mnemonic": "LDA #${:02X}",
            "full_name": "LoaD Accumulator",
            "effect": "A,Z,N = M",
            "addressing_mode": AddressingMode.IMMEDIATE,
            "num_bytes": 2,
        },
        0xAD: {
            "mnemonic": "LDA ${:04X}",
            "full_name": "LoaD Accumulator",
            "effect": "A,Z,N = M",
            "addressing_mode": AddressingMode.ABSOLUTE,
            "num_bytes": 3,
        },
        0xB0: {
            "mnemonic": "BCS ${:d}",
            "full_name": "Branch on Carry Set",
            "effect": "IF [C == 1]; Update PC",
            "addressing_mode": AddressingMode.RELATIVE,
            "num_bytes": 2,
        },
        0xBD: {
            "mnemonic": "LDA ${:04X},X",
            "full_name": "LoaD Accumulator",
            "effect": "A,Z,N = M",
            "addressing_mode": AddressingMode.ABSOLUTE_X,
            "num_bytes": 3,
        },
        0xC9: {
            "mnemonic": "CMP ${:02X}",
            "full_name": "LoaD Accumulator",
            "effect": "Z,C,N = A-M",
            "addressing_mode": AddressingMode.IMMEDIATE,
            "num_bytes": 2,
        },
        0xCA: {
            "mnemonic": "DEX",
            "full_name": "DEcrement X register",
            "effect": "X,Z,N = X-1",
            "addressing_mode": AddressingMode.IMPLIED,
            "num_bytes": 1,
        },
        0xD0: {
            "mnemonic": "BNE ${:d}",
            "full_name": "Branch if Not Equal",
            "effect": "IF [Z == 0]; Update PC",
            "addressing_mode": AddressingMode.RELATIVE,
            "num_bytes": 2,
        },
        0xD8: {
            "mnemonic": "CLD",
            "full_name": "CLear Decimal mode",
            "effect": "D = 0",
            "addressing_mode": AddressingMode.IMPLIED,
            "num_bytes": 1,
        }
}


def twos_comp(val):
    if (val & (1 << 7)) != 0:
        val -= (1 << 8)
    return val


class Instruction():
    opcode = None
    mnemonic = None
    full_name = None
    effect = None
    addressing_mode = None
    byte_list = []

    def __init__(self, byte_list):
        self.opcode = byte_list[0]
        self.mnemonic = OPCODES[self.opcode].get('mnemonic', None)
        self.full_name = OPCODES[self.opcode].get('full_name', None)
        self.effect = OPCODES[self.opcode].get('effect', None)
        self.addressing_mode = OPCODES[self.opcode].get('addressing_mode',
                                                        None)
        self.byte_list = byte_list

    def __str__(self):
        if self.addressing_mode == AddressingMode.IMPLIED:
            return self.mnemonic
        elif self.addressing_mode == AddressingMode.IMMEDIATE:
            return self.mnemonic.format(self.byte_list[1])
        elif self.addressing_mode in (AddressingMode.ABSOLUTE,
                                      AddressingMode.ABSOLUTE_X):
            addr = (self.byte_list[2] << 8) | (self.byte_list[1])
            return self.mnemonic.format(addr)
        elif self.addressing_mode == AddressingMode.RELATIVE:
            displacement = twos_comp(self.byte_list[1])
            return self.mnemonic.format(displacement)


def decode(memory, address):
    opcode = memory[address]

    if opcode not in OPCODES:
        print("Opcode {} not supported".format(hex(opcode)), file=sys.stderr)
        sys.exit(1)

    num_bytes = OPCODES[opcode]['num_bytes']

    return Instruction(memory[address:address+num_bytes])
