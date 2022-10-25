import random

s1 = ['+', '-', '*', '/']
s2 = ['+', '-', '*', '/', '^']
l = int(input('Выберите уровень(1-2): '))
if l == 1:
    count = 0
    for i in range(10):
        c1, c2, c3 = random.randrange(1, 10), random.choice(s1), random.randrange(1, 10)
        if c2 == '+':
            o = c1 + c3
        if c2 == '-':
            o = c1 - c3
        if c2 == '*':
            o = c1 * c3
        if c2 == '/':
            o = c1 / c3
        print(c1, c2, c3, '=')
        q = input('Введите ответ: ')
        if q != str(round(o, 1)) or q != str(round(o, 2)):
            print('Неверно!')
        else:
            print('Верно!')
            count += 1
    print(f'Ваш результат: {count}/10 ')
    if count < 3:
        print('Слабенько(')
    if 3 < count < 7:
        print('Удовлетворительно :/')
    if count > 7:
        print('А ты хорош ;D')
else:
    count = 0
    for i in range(10):
        c1, c2, c3 = random.randrange(1, 1000), random.choice(s1), random.randrange(1, 1000)
        if c2 == '+':
            o = c1 + c3
        if c2 == '-':
            o = c1 - c3
        if c2 == '*':
            o = c1 * c3
        if c2 == '/':
            o = c1 / c3
        if c2 == '^':
            o = c1**c3
        print(c1, c2, c3, '=')
        q = input('Введите ответ: ')
        if q != str(round(o, 1)) or q != str(round(o, 2)):
            print('Неверно!')
        else:
            print('Верно!')
            count += 1
    print(f'Ваш результат: {count}/10 ', end='')
    if count < 3:
        print('Слабенько(')
    if 3 < count < 7:
        print('Удовлетворительно :/')
    if count > 7:
        print('А ты хорош ;D')

