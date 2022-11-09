def read_file(filename):
    '''Читает файл, выдает сортированный список содержащихся в нем уникальных слов.'''
    res = set()
    with open(filename, mode='r', encoding='utf8') as infile:
        # файлы могут быть большие и read в этом случае прочитает только кусок,
        # возможно оборванный в середине слова
        for line in infile:
            res.update(word.strip('.,:;\'"()').lower() for word in line.split())
    return sorted(res)


def save_file(filename, wordlist):
    '''Записывает в файл длину списка слов и слова из него, по одному на строке'''
    count = len(wordlist)
    with open(filename, mode='w', encoding='utf8') as outfile:
        outfile.write(f'{count}\n')
        for w in wordlist:
            print(w, file=outfile)

save_file('spis-output.txt', read_file('spis-input.txt'))
