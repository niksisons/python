def a1(n):


def a2(n):


def a3(n):



def a4(n):


print('1. Добавить контакт', '2. Удалить контакт', '3. Просмотреть телефонную книгу', '4. Изменить номер телефона (по имени)', sep='\n')
n = input('Выберите функцию: ')
sl = {}
if n == 1:
    print(a1(input()))
if n == 2:
    print(a2(input()))
if n == 3:
    print(a3(input()))
if n == 4:
    print(a4(input()))