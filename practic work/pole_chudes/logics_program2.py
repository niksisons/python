import file_read



def game():
    global rec
    global point
    sl1 = file_read.slova()
    black_box = ['\u25A0' for i in range(len(sl1))]
    print(f'Ваш текущий рекорд: {rec}')
    complexity = int(input('Выберите сложность(1, 2, 3): '))
    if complexity == 1:
        lives = 7
    elif complexity == 2:
        lives = 5
    else:
        lives = 3
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
                print('Верно:D')
                break
            else:
                print('Неверное слово')
                lives -= 1
                count -= 1
    continues = int(input('Желаете продолжить?(1, 0): '))
    if continues:
        point += count
        game()
    else:
        point += count
        if point > rec:
            file_read.writed(str(point))
        print(f'Игра окончена. Ваш результат: {point}.')


rec = file_read.records()
point = 0

game()
