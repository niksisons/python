import random

operation1 = ['+', '-', '*', '/']
operation2 = ['+', '-', '*', '/', '^']
complexity: int = int(input('Выберите уровень(1-2): '))
if complexity == 1:
    count: int = 0
    for i in range(10):
        chislo1, chislo2, chislo3 = random.randrange(1, 10), random.choice(operation1), random.randrange(1, 10)
        if chislo2 == '+':
            rez: float = chislo1 + chislo3
        if chislo2 == '-':
            rez: float = chislo1 - chislo3
        if chislo2 == '*':
            rez: float = chislo1 * chislo3
        if chislo2 == '/':
            rez: float = chislo1 / chislo3
        print(chislo1, chislo2, chislo3, '=')
        q: str = input('Введите ответ: ')
        if q != str(round(rez, 1)) or q != str(round(rez, 2)):
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
    count: int = 0
    for i in range(10):
        chislo1, chislo2, chislo3 = random.randrange(1, 1000), random.choice(operation1), random.randrange(1, 1000)
        if chislo2 == '+':
            rez: float = chislo1 + chislo3
        if chislo2 == '-':
            rez: float = chislo1 - chislo3
        if chislo2 == '*':
            rez: float = chislo1 * chislo3
        if chislo2 == '/':
            rez: float = chislo1 / chislo3
        if chislo2 == '^':
            rez: float = chislo1**chislo3
        print(chislo1, chislo2, chislo3, '=')
        q: str = input('Введите ответ: ')
        if q != str(round(rez, 1)) or q != str(round(rez, 2)):
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

