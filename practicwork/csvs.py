import csv


def get_book(pyythin):
    with open('books.csv', newline='', encoding='utf8') as f:
        catalog = csv.reader(f, delimiter='|', quotechar=',')
        rez = [row if pyythin in row else '' for row in catalog]
        return rez


def get_totals(py):
    rez = [(i[0], int(i[-1])*int(i[-2]) if int(i[-1])*int(i[-2]) >= 500 else int(i[-1])*int(i[-2]) + 100) for i in py]
    return rez


# print(get_book('Dow'))
print(get_totals(get_book('Dow')))








