import random


def p(n):
    rez1 = 0
    rez2 = 0
    rez3 = 0
    rez4 = 0
    for i in range(n):
        three_door = [0, 0, 1]
        player = random.choice(three_door)
        two_door = three_door[1:]
        two_step_player = random.choice(two_door)
        if player == 1 and two_step_player == 1:
            rez1 += 1
        if player == 0 and two_step_player == 1:
            rez2 += 1
        if player == 1 and two_step_player == 0:
            rez3 += 1
        if player == 0 and two_step_player == 0:
            rez4 += 1
    return (rez1 / 100), (rez2 / 100), (rez3 / 100), (rez4 / 100), f'Ответ: {((rez1 + rez2 + rez3) / 100)}'


print(p(10001))
