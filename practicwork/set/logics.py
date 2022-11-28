def read_file() -> list[str]:
    '''
    :return: список слов из файла без разделительных знаков и символов.
    '''
    with open('spis-input.txt', 'r', encoding='utf8') as sp1:
        z: any = str.maketrans('''!()-[]{};?@#$%:'"\,./^&amp;*_''', '                             ')
        r: list = sp1.read().lower().translate(z).split()
        return [i + '\n' for i in r]
        # return [i.replace('.', '').replace(',', '') + '\n' if '.' in i or ',' in i else i + '\n' for i in sp1.read()
        #     .lower().split()]


def save_file(c: int, n: list):
    '''
    :param c: Количество слов в файле(int).
    :param n: Список со всеми словами из текста.
    :return: -
    '''
    with open('spis-output.txt', 'w', encoding='utf8') as sp2:
        sp2.write(str(c) + '\n')
        sp2.writelines(n)


def start():
    '''
    :return: -
    '''
    inputs: list = sorted(set(read_file()))
    count: int = len(inputs)
    save_file(count, inputs)


start()
