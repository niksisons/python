def normalizator():
    no = input('Введите номер: ')
    no = no.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    while not no[1:].isdigit():
        no = input('Неверно введен номер: ')
    else:
        if len(no) == 12:
            return no
        if len(no) == 11:
            return no.replace(no[0], '+7', 1)
        if len(no) == 10:
            return '+7' + no
        else:
            print('Неверно введен номер: ')
            return normalizator()


def norm():
    a = input('Введите ФИО: ').split()
    return ' '.join(a).title()


def a1():
    sl[norm()] = normalizator()
    return 'Контакт сохранён'


def a2(n):
    if sl[n] in sl:
        del sl[n]
        return 'Успешно'
    else:
        return 'Контакт не существует'


def a3():
    for b, c in sl.items():
        print(b, c)


def a4():
    n = norm()
    if sl.get(n) == None:
        return 'Такого контакта нет'
    else:
        sl[n] = normalizator()
        return 'Успешно'


sl = {}

while True:
    print('1. Добавить контакт', '2. Удалить контакт', '3. Просмотреть телефонную книгу', '4. Изменить номер телефона (по имени)', '5. Выйти', sep='\n')
    n = input('Выберите функцию: ')

    if n == '1':
        print(a1())
    if n == '2':
        print(a2(norm()))
    if n == '3':
        a3()
    if n == '4':
        print(a4())
    if n == '5':
        print('Спасибо за использование:D')
        print(*sl)
        break
