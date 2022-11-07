import random

while True:
    with open(r'C:\Users\nikita\PycharmProjects\python\practic work\pole_chudes\slova.txt', encoding='UTF8') as sl:
        sl1 = random.choice(sl.read().splitlines()).lower()
        black_box = ['\u25A0' for i in range(len(sl1))]
    with open(r'C:\Users\nikita\PycharmProjects\python\practic work\pole_chudes\records.txt', mode='r+',
              encoding='UTF8') as r:
        rec = int(r.read())
        print(f'Ваш текущий рекорд: {rec}')
        complexity = int(input('Выберите сложность(1, 2, 3, 4-Выйти): '))
        if complexity == 1:
            lives = 7
        elif complexity == 2:
            lives = 5
        elif complexity == 3:
            lives = 3
        else:
            break
        count = len(sl1)
        while black_box.count('\u25A0') and lives:
            n = input(f'Назовите букву: {"".join(black_box)}\n')
            if len(n) == 1:
                if n in sl1.lower():
                    black_box = [n if n == sl1[i] else black_box[i] for i in range(len(sl1))]
                    count -= 1
                else:
                    print('Такой буквы нет')
                    lives -= 1
            else:
                if n.lower() == sl1.lower():
                    break
                else:
                    print('Неверное слово')
                    lives -= 1
                    count -= 1
        rec += count
        if count > rec:
            r.seek(0)
            r.write(str(rec))
print(f'Игра окончена. Ваш результат: {count}.\nЛучший: {rec}')
