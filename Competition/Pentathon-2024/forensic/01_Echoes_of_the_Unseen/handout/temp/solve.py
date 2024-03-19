def find_iend(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        iend_offset = data.rfind(b'IEND')
        return iend_offset + len(b'IEND') + 4

def remove_extra_data(file_path, output_path):
    iend_offset = find_iend(file_path)
    with open(file_path, 'rb') as input_file:
        with open(output_path, 'wb') as op:
            op.write(input_file.read(iend_offset))


# Example usage:
ip = 'tmp.png'
op = 'new_file.png'
remove_extra_data(ip, op)

