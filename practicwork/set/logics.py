def read_file():
    with open('spis-input.txt', 'r', encoding='utf8') as sp1:
        return [i.replace('.', '').replace(',', '') + '\n' if '.' in i or ',' in i else i + '\n' for i in sp1.read()
            .lower().split()]


def save_file(c, n):
    with open('spis-output.txt', 'w', encoding='utf8') as sp2:
        sp2.write(str(c) + '\n')
        sp2.writelines(n)


inputs = sorted(set(read_file()))
count = len(inputs)
save_file(count, inputs)

