import os


def list_file(*args):
    files = []
    files_c = []
    for filename in os.listdir(start_directory()):
        if filename.endswith(args):
            files.append(filename)
    for filename in enumerate(files, start=1):
        files_c.append(filename)
    return files_c


def start_directory():  # path
    return os.getcwd()


def directory():  # 0
    n = input('Введите путь: ')
    while n == '':
        n = input('Введите путь: ')
    os.chdir(n)
    return 'Успех'


def del_extension():
    print(list_file())
    extension = input('Введите расширение: ')
    if extension != '0':
        for i in list_file(''):
            if i[1].endswith(extension) and '_' in i[1]:
                os.rename(i[1], i[1].split('_')[1])
        return 'Успех'
    else:
        return


print(directory())
print(start_directory())
print(del_extension())
