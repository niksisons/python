import random

while True:
    with open(r'C:\Users\nikita\PycharmProjects\python\practic work\pole_chudes\slova.txt', encoding='UTF8') as sl:
        sl1 = random.choice(sl.read().splitlines())
        black_box = ['\u25A0' for i in range(len(sl1))]
    with open(r'C:\Users\nikita\PycharmProjects\python\practic work\pole_chudes\records.txt', mode='a+',
              encoding='UTF8') as r:
        rec = r.read()
        print(f'Ваш прошлый рекорд: {rec}')
        complexity = int(input('Выберите сложность(1, 2, 3, 4-Выйти): '))
        if complexity == 1:
            lives = 7
        elif complexity == 2:
            lives = 5
        elif complexity == 3:
            lives = 3
        else:
            break
        count = 0
        while count != len(sl1):
            if lives == 0:
                break
            n = input(f'Назовите букву: {"".join(black_box)}\n')
            if len(n) == 1:
                if n in sl1.lower():
                    ind = sl1.lower().index(n)
                    if black_box[ind] == n:
                        continue
                    black_box[ind] = n
                    count += 1
                else:
                    print('Такой буквы нет')
                    lives -= 1
            else:
                if n.lower() == sl1.lower():
                    count += len(sl1)
                    break
                else:
                    print('Неверное слово')
                    lives -= 1
        if count > int(rec):
            rec = str(count)
            r.write(rec)
print(f'Игра окончена. Ваш результат: {count}.\nЛучший: {rec}')
