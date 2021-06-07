"""The file provides a command line interface for the tool"""


import argparse
import exploit.file_inspection_evasion as fie

if __name__ == '__main__':
    msg = "This is a command line tool as a PoC of some anti virus evading techniques"

    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("-f", "--File", required=True, help="zip File to edit")
    parser.add_argument("-g", "--ghost", action='store_true',
                        help="use ghost file technique")
    parser.add_argument("-i", "--invalid_header", action='store_true',
                        help="use invalid file header technique")
    parser.add_argument("-b", "--buffer_collapsing",
                        action='store_true', help="use buffer collapsing technique")

    args = parser.parse_args()

    technique = []

    if args.ghost:
        technique.append('ghost')
    if args.invalid_header:
        technique.append('invalid_header')
    if args.buffer_collapsing:
        technique.append('buffer_collapsing')

    if len(technique) == 0:
        print('Evasion Technique Required')

    if args.File and technique:
        fie.evade(file_loc=args.File, techniques=technique)
