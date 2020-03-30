import os
import sys

NES_FILE_SIGNATURE = b"NES\x1a"
NES_FILE_HEADER_SIZE = 16
NES_FILE_TRAINER_SIZE = 512


class NESFileHeader():
    prg_rom_size = 0
    chr_rom_size = 0
    chr_ram_used = False
    vertical_mirroring = False
    cartridge_prg_ram = False
    trainer = False
    ignore_mirroring = False
    mapper = 0
    vs_unisystem = False
    playchoice_10 = False
    nes2_format = False

    def parse_header_flag_6(self, byte):
        bitstring = bin(byte).lstrip('0b').zfill(8)[::-1]
        self.vertical_mirroring = (bitstring[0] == '1')
        self.cartridge_prg_ram = (bitstring[1] == '1')
        self.trainer = (bitstring[2] == '1')
        self.ignore_mirroring = (bitstring[3] == '1')
        self.mapper = int(bitstring[4:8][::-1], base=2)

    def parse_header_flag_7(self, byte):
        bitstring = bin(byte).lstrip('0b').zfill(8)[::-1]
        self.vs_unisystem = (bitstring[0] == '1')
        self.playchoice_10 = (bitstring[1] == '1')
        self.nes2_format = (bitstring[2:3][::-1] == '10')
        self.mapper = (int(bitstring[4:8][::-1], base=2) << 4) | self.mapper

    def __init__(self, header):
        if header[:4] != NES_FILE_SIGNATURE:
            print("Invalid file signature", file=sys.stderr)
            sys.exit(1)

        self.prg_rom_size = header[4] * 16 * 1024
        self.chr_rom_size = header[5] * 8 * 1024
        if header[5] == 0:
            self.chr_ram_used = True
        self.parse_header_flag_6(header[6])
        self.parse_header_flag_7(header[7])

    def __str__(self):
        output = []
        output.append(f"PRG ROM size: {self.prg_rom_size}")
        if self.chr_ram_used:
            output.append("CHR RAM used")
        else:
            output.append(f"CHR ROM size: {self.chr_rom_size}")
        if self.vertical_mirroring:
            output.append("Vertical mirroring (horizontal arrangement) "
                          "(CIRAM A10 = PPU A10)")
        else:
            output.append("Horizontal mirroring (vertical arrangement) "
                          "(CIRAM A10 = PPU A11)")
        if self.cartridge_prg_ram:
            output.append("Cartridge contains battery-backed PRG RAM "
                          "($6000-$7FFF) or other persistent memory")
        if self.trainer:
            output.append("512 byte trainer at $7000-$71FF "
                          "(stored before PRG data)")
        if self.ignore_mirroring:
            output.append("Ignore mirroring control or above mirroring bit; "
                          "instead provide four-screen VRAM")
        if self.vs_unisystem:
            output.append("VS Unisystem")
        if self.playchoice_10:
            output.append("PlayChoice-10 "
                          "(8KB of Hint Screen data stored after CHR data)")
        if self.nes2_format:
            output.append("NES 2.0 file format")

        output.append(f"Mapper number: {self.mapper}")
        return "\n".join(output)


class NESFile():
    header = None
    trainer = None
    prg_rom = None
    prg_rom_offset = None
    trainer = None
    chr_rom = None

    def check_file(self, filename):
        if not os.path.exists(filename):
            print("File does not exist: {}".format(filename), file=sys.stderr)
            sys.exit(1)

    def update_mapper(self):
        if self.header.mapper != 0:
            print("Mapper not supported: {}".format(self.header.mapper),
                  file=sys.stderr)
            sys.exit(1)

        self.prg_rom_offset = 0x8000

    def __init__(self, filename):
        self.check_file(filename)

        with open(filename, "rb") as nes_file:
            self.header = NESFileHeader(nes_file.read(NES_FILE_HEADER_SIZE))
            self.update_mapper()

            if self.header.trainer:
                self.trainer = nes_file.read(NES_FILE_TRAINER_SIZE)

            self.prg_rom = nes_file.read(self.header.prg_rom_size)

            if not self.header.chr_ram_used:
                self.chr_rom = nes_file.read(self.header.chr_rom_size)

    def __str__(self):
        return "Not implemented yet"
