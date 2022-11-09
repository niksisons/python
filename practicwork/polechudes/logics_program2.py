from .fileread import *

def game():
    rec = records()
    point = 0
    sl1 = slova()
    black_box = ['\u25A0'] * len(sl1)
    print(f'Ваш текущий рекорд: {rec}')
    complexity = int(input('Выберите сложность(1, 2, 3): '))
    if complexity == 1:
        lives = 7
    elif complexity == 2:
        lives = 5
    else:
        lives = 3
    count = len(set(sl1))   # А если там одинаковые буквы?
    while '\u25A0' in black_box and lives:
        n = input(f'Назовите букву: {"".join(black_box)}\n').lower()
        count -= 1   # Попытка использована, угадал или нет - уже другой вопрос
        if len(n) == 1:
            if n in sl1:
                black_box = [n if n == char else black_box[i] for i, char in enumerate(sl1)]
            else:
                print('Такой буквы нет')
                lives -= 1
        else:
            if n == sl1:
                print(f'Верно:D, {sl1}')
                break
            else:
                print('Неверное слово')
                lives -= 1
    else:
        print(f'Верно:D, {sl1}')

    point += count
    if point > rec:
        rec = point

    continues = int(input('Желаете продолжить?(1, 0): '))
    if continues:
        game()
    else:
        writed(str(rec))
        print(f'Игра окончена. Ваш результат: {point}.')
