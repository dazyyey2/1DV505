import os


def print_files(dir_path):
    entries = os.scandir(dir_path)
    for e in entries:
        if e.is_file():
            if not is_hidden(e):
                print('\nFile: ' + e.name)
                print('File Path: ' + e.path)
        elif e.is_dir():
            if not is_hidden(e):
                print_files(e.path)


def is_hidden(entry):
    if entry.name.startswith('.') or entry.name.startswith('_'):
        return True
    return False


dir_path = input('Enter directory (leave blank for cwd): ')
if dir_path == '':
    dir_path = os.getcwd()
    print(f'Current directory is {dir_path}')
print_files(dir_path)
