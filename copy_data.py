import shutil
from common import get_source_file_list, get_destination_file_list

DATA_DIRECTORY = './data'


def copy_files():
    source_files = get_source_file_list()
    destination_files = get_destination_file_list()

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


if __name__ == '__main__':
    copy_files()
