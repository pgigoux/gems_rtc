import shutil
from common import DATA_FOLDER, get_source_file_list, get_destination_file_list


def copy_files(directory=DATA_FOLDER):
    """
    Copy files from the RTC area into the data directory. The files in the RTC area
    always have the same name. The destination files will have a time stamp in their
    names to avoid overwriting files.
    :param: directory: directory where to write files (default=DATA_FOLDER)
    :return: None
    """
    source_files = get_source_file_list()
    destination_files = get_destination_file_list(directory=directory)

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
