#!/usr/bin/env python3

import argparse
import NESFile
import instructions


def read_bytes(filename, start, num_bytes):
    with open(filename, "rb") as nes_file:
        nes_file.seek(start)
        bytes_read = nes_file.read(num_bytes)

    return bytes_read


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Tool to disassemble .nes files'
    )
    parser.add_argument('file', type=str, help='.nes file to decompile')
    parser.add_argument('--headers', action='store_true')

    return parser.parse_args()


def main():
    args = parse_arguments()

    nes_file = NESFile.NESFile(args.file)

    if args.headers:
        print("============= HEADER =============")
        print(nes_file.file_header)
    else:
        print("============ PRG ROM ============")
        address = 0
        while address < len(nes_file.prg_rom):
            instruction = instructions.decode(nes_file.prg_rom, address)
            print("${:04x}: {}".format(address, instruction))
            address += len(instruction.byte_list)


if __name__ == '__main__':
    main()
