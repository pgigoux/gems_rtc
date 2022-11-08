#!/usr/bin/env python
import sys
from argparse import ArgumentParser
import fileio


def check_files(file_list: list, reference_value: int):
    """
    :param file_list: file list to process
    :param reference_value: value to compare the value contents with
    :return:
    """
    n = 35
    for file_name in file_list:
        m = fileio.MemoryDumpFile(file_name)
        count = 0
        for word in m.get_next_word():
            msw, lsw = m.split_words(word)
            if msw != reference_value or lsw != reference_value:
                count += 1
        m.close_file()
        print(f'{file_name:35} {count:>7d} discrepancies')


def get_args(argv):
    """
    Process command line arguments
    :param argv: command line arguments from sys.argv
    :type argv: list
    :return: arguments
    :rtype: argparse.Namespace
    """

    parser = ArgumentParser()

    parser.add_argument(action='store',
                        dest='files',
                        default=[],
                        nargs='+',
                        help=f'file list to process')

    parser.add_argument('-v',
                        action='store',
                        dest='value',
                        default=0,
                        help=f'value to match default=0')

    return parser.parse_args(argv[1:])


if __name__ == '__main__':
    args = get_args(sys.argv)
    check_files(args.files, int(args.value))
