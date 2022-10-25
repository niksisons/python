import random


def a(ludi, gr):
    count = 0
    for i in range(gr):
        sp = []
        for p in range(ludi):
            sp.append(random.randint(1, 364))
        if len(set(sp)) != ludi:
            count += 1
    return count/(gr/100)


print(a(60, 1000), '%', sep='')
