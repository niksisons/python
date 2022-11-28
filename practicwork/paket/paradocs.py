import random


def paradocs(ludi: int, gr: int) -> float:
    '''
    :param ludi: Количество человек в группе.
    :param gr: Количество групп.
    :return: Вероятность того, что у этого количества человек в группе совпадут дни рождения.
    '''
    count = 0
    for i in range(gr):
        sp = []
        for p in range(ludi):
            sp.append(random.randint(1, 364))
        if len(set(sp)) != ludi:
            count += 1
    return count/(gr/100)


print(paradocs(60, 1000), '%', sep='')
