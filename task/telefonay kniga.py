def normalizator(no):
    no = no.replace('-', '').replace(' ', '')
    while not no.isdigit():
        print('Неверно введен номер')
        no = input()
    else:
        while len(no) != 12:
            if len(no) == 11:
                return no.replace(no[0], '+7', 1)
            if len(no) == 10:
                return '+7' + no
            no = input('Введите номер: ')
        return no


def a1(n):
    sl[input('ФИО: ').title()] = normalizator(input('Введите номер: '))
    return 'Контакт сохранён'

def a2(n):
    if sl[n] in sl:
        del sl[n]
        return 'Успешно'
    else:
        return 'Контакт не существует'


def a3(n):
    for b, c in sl.items():
        print(b, c)


def a4(n):
    if sl.get(n) == None:
        return 'Такого контакта нет'
    else:
        sl[n] = normalizator(input('Введите новый номер: '))
        return 'Успешно'


sl = {}

while True:
    print('1. Добавить контакт', '2. Удалить контакт', '3. Просмотреть телефонную книгу', '4. Изменить номер телефона (по имени)', '5. Выйти', sep='\n')
    n = input('Выберите функцию: ')

    if n == '1':
        print(a1(n))
    if n == '2':
        print(a2(input('Введите имя: ').title()))
    if n == '3':
        a3(sl)
    if n == '4':
        print(a4(input('Введите имя: ').title()))
    if n == '5':
        print('Спасибо за использование:D')
        print(*sl)
        break
