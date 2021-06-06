"""The main file to run the program from the command line"""


import argparse
import exploit.file_inspection_evasion as fie


# def main(file_loc):
#     """The main function for the program

#     Args:
#         file_loc (str): The location of the original zip file for the exploit
#     """
#     original_file_hex = fie.read_in_file(file_loc)
#     local_files, central_directory, end_central_directory = fie._split_zip_file_into_sections(
#         original_file_hex)
#     # print('\n\n\n')
#     # print(original_file_hex)
#     # print('\n\n\n')
#     # print(local_files)
#     # print('\n\n\n')
#     # print(central_directory)
#     # print('\n\n\n')
#     # print(end_central_directory)
#     # print('\n\n\n')
#     invalid_file_header = ('504b03040a0000000000000000006745'
#                            '23010000000000000000ffff0000612f'
#                            '2f2f642f')
#     # fie.write_out_file(file_loc=file_loc,
#     #                    contents=f'{local_files}')
#     fie.write_out_file(file_loc=file_loc,
#                        contents=f'{invalid_file_header}{local_files}')


#  TODO Look up argparser examples
if __name__ == '__main__':
    # TODO update the description
    msg = "Test Description can select multiple techniques default is ghost"

    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("-f", "--File", required=True, help="zip File to edit")
    parser.add_argument("-g", "--ghost", action='store_true',
                        help="use ghost file technique")
    parser.add_argument("-i", "--invalid_header", action='store_true',
                        help="use invalid file header technique")

    args = parser.parse_args()

    technique = {}
    if args.ghost:
        technique['ghost'] = True
    if args.invalid_header:
        technique['invalid_header'] = True

    if not args.ghost and not args.invalid_header:
        technique['ghost'] = True
        print("not ghost")

    if technique:
        print(technique)
    if not technique:
        print('no technique')
    print(args)

    if args.File:
        fie.main(file_loc=args.File, techniques=technique)
