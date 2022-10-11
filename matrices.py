from common import get_process_file_list


def process_file(file_name: str, print_header: bool = False, reference_value=0):
    """
    Process a single memory dump file. This routine assumes a healthy file will contain
    a constant value
    :param: file_name: name of file to process
    :param: print_header: print the header information in the file
    :param: reference_value: reference used to detect bad data
    :return: None
    """
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('file not found', file_name)
        return

    # address = 0
    count = 0

    for line in f:
        line = line.strip()

        # The file header lines start with a semicolon
        if line.find(';') > -1:
            if print_header:
                print(line)
            # Extract the starting address, number of words and file name from the header
            if line.find('diag21k') > -1:
                # print('found diag21k')
                _, _, _, _, address_hex, number_of_words, name = line.split()
                # print(address, count, name)
                address = int(address_hex, 16)
                number_of_words = int(number_of_words)
                ending_address = hex(address + number_of_words)
                # print(f'Processing file {name}, starting address 0x{address_hex}, number of words {number_of_words}')
                # print(f'    Starting address 0x{address_hex}')
                # print(f'    Number of words {number_of_words}')
                # print(f'    Ending address {ending_address}')
        else:
            # process values
            line = line.replace('0x', '')
            value = int(line, 16)
            # count number of discrepancies
            if value != reference_value:
                count += 1

    f.close()

    print(f'{file_name}: found {count} discrepancies')


if __name__ == '__main__':
    print(get_process_file_list('20220928114409'))
    for file in get_process_file_list('20220928114409'):
        process_file(file)
        print('-' * 70)
