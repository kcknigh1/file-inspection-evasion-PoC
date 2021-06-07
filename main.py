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

    technique = {}
    if args.ghost:
        technique['ghost'] = True
    if args.invalid_header:
        technique['invalid_header'] = True
    if args.buffer_collapsing:
        technique['buffer_collapsing'] = True

    if len(technique) == 0:
        print('Evasion Technique required')

    if args.File and technique:
        fie.main(file_loc=args.File, techniques=technique)
