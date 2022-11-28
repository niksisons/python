def normalizator() -> str:
    '''
    :return: Нормализованный номер телефона в виде строки.
    '''
    numbers: str = input('Введите номер: ')
    numbers: str = numbers.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
    while not numbers[1:].isdigit():
        numbers: str = input('Неверно введен номер: ')
    else:
        if len(numbers) == 12:
            return numbers
        if len(numbers) == 11:
            return numbers.replace(numbers[0], '+7', 1)
        if len(numbers) == 10:
            return '+7' + numbers
        else:
            print('Неверно введен номер: ')
            return normalizator()


def norm() -> str:
    a: list[str] = input('Введите ФИО: ').split()
    return ' '.join(a).title()


def add_num() -> str:
    sl[norm()]: str = normalizator()
    return 'Контакт сохранён'


def delite_num(fio: str) -> str:
    if fio in sl:
        del sl[fio]
        return 'Успешно'
    else:
        return 'Контакт не существует'


def print_list():
    for fio, num in sl.items():
        print(fio, num)


def edit_num() -> str:
    fio: str = norm()
    if sl.get(fio) == None:
        return 'Такого контакта нет'
    else:
        sl[fio] = normalizator()
        return 'Успешно'


sl: dict = {}

while True:
    print('1. Добавить контакт', '2. Удалить контакт', '3. Просмотреть телефонную книгу', '4. Изменить номер телефона (по имени)', '5. Выйти', sep='\n')
    param: str = input('Выберите функцию: ')

    if param == '1':
        print(add_num())
    if param == '2':
        print(delite_num(norm()))
    if param == '3':
        print_list()
    if param == '4':
        print(edit_num())
    if param == '5':
        print('Спасибо за использование:D')
        print(*sl)
        break
