#!/usr/bin/env python
import sys
from argparse import ArgumentParser
import fileio


def calculate_statistics(file_list: list):
    """
    :param file_list: file list to process
    :return:
    """
    min_value = 99999999
    max_value = -9999999
    sum_value = 0
    sum_value2 = 0
    print('# Values are min, max, avarage, stddev^2 and count')
    for file_name in file_list:
        m = fileio.MemoryDumpFile(file_name)
        count = 0
        for word in m.get_next_word():
            msw, lsw = m.split_words(word)
            min_value = min(min(min_value, msw), lsw)
            max_value = max(max(max_value, msw), lsw)
            sum_value += (msw + lsw)
            sum_value2 += (msw ** 2 + lsw ** 2)
            count += 2
        avg = float(sum_value) / float(count)
        avg2 = float(sum_value2) / float(count)
        sdev = avg2 - avg ** 2
        m.close_file()
        print(f'{min_value:>5d} {max_value:>5d}  {avg:>9.3e} {sdev:>9.3e} {count:>7d}')

        break


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

    return parser.parse_args(argv[1:])


if __name__ == '__main__':
    args = get_args(sys.argv)
    calculate_statistics(args.files)
