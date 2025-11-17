import os


def count_lines(path, depth):
    depth_indent = '    '
    entries = os.scandir(path)
    for e in entries:
        if e.is_file():
            if not is_hidden(e):
                if is_python(e):
                    print(f'{depth_indent*depth + e.name}\
                        ({compute_lines(e.path)} lines)')
                else:
                    print(depth_indent*depth + e.name)
        elif e.is_dir():
            if not is_hidden(e):
                print(depth_indent*depth + e.name)
                count_lines(e.path, depth + 1)


def compute_lines(file):
    counter = 0
    with open(file, 'r') as file_stream:
        for line in file_stream:
            if line.strip() != '':
                counter += 1
    return counter


def is_python(entry):
    if entry.name.endswith('.py'):
        return True
    return False


def is_hidden(entry):
    if entry.name.startswith('.') or entry.name.startswith('_'):
        return True
    return False


dir_path = input('Enter directory (leave blank for cwd): ')
if dir_path == '':
    dir_path = os.getcwd()
    print(f'Current directory is {dir_path}')
count_lines(dir_path, 0)
