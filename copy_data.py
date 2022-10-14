#!/usr/bin/env python
import os
import sys
import shutil
from argparse import ArgumentParser
from common import DEFAULT_SOURCE_FOLDER, DESTINATION_DATA_FOLDER, get_source_file_list, get_destination_file_list


def copy_files(source_directory=DEFAULT_SOURCE_FOLDER, destination_directory=DESTINATION_DATA_FOLDER):
    """
    Copy files from the RTC area into the data directory. The files in the RTC area
    always have the same name. The destination files will have a time stamp in their
    names to avoid overwriting files.
    :param: source_directory: directory where the file will be copied from
    :param: destination_directory: directory where the files will be written to
    :return: None
    """
    source_files = get_source_file_list(source_directory=source_directory)
    destination_files = get_destination_file_list(source_directory=source_directory,
                                                  destination_directory=destination_directory)
    # print(source_files)
    # print(destination_files)

    # Sanity check
    if len(source_files) != len(destination_files):
        raise ValueError('source and destination lists are of different length')

    # Copy files
    for source, destination in zip(source_files, destination_files):
        print(f'Copying {source} to {destination}')
        try:
            shutil.copyfile(source, destination)
        except FileNotFoundError:
            print(f'{source} does not exist')
        except PermissionError:
            print(f'Cannot write {destination}')


def get_args(argv):
    """
    Process command line arguments
    :param argv: command line arguments from sys.argv
    :type argv: list
    :return: arguments
    :rtype: argparse.Namespace
    """

    parser = ArgumentParser()

    parser.add_argument('-s',
                        action='store',
                        dest='source',
                        default=f'default=[{DEFAULT_SOURCE_FOLDER}]',
                        help=f'source folder default=[{DEFAULT_SOURCE_FOLDER}]')

    parser.add_argument('-d',
                        action='store',
                        dest='destination',
                        default=os.path.join('.', 'data'),
                        help=f'destination data folder default=[{DESTINATION_DATA_FOLDER}]')

    return parser.parse_args(argv[1:])


if __name__ == '__main__':
    args = get_args(sys.argv)
    print(args.source, args.destination)
    copy_files(source_directory=args.source, destination_directory=args.destination)
