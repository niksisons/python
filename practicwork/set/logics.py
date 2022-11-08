def read_file():
    with open('spis-input.txt', mode='r', encoding='utf8') as sp1:
        spis_in = [i for i in sp1.read().split()]
        return spis_in


def save_file(c, n):
    with open('spis-output.txt', mode='a', encoding='utf8') as sp2:
        sp2.write(str(c) + '\n')
        sp2.writelines(n)


inputs = sorted([i.lower() + '\n' for i in set(read_file())])
count = len(inputs)
save_file(count, inputs)
