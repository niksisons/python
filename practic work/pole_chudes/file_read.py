import random


def slova():
    with open(r'C:\Users\nikita\PycharmProjects\python\practic work\pole_chudes\slova.txt', encoding='UTF8') as sl:
        return random.choice(sl.read().splitlines()).lower()


def records():
    with open(r'C:\Users\nikita\PycharmProjects\python\practic work\pole_chudes\records.txt', mode='r',
              encoding='UTF8') as r:
        return int(r.read())


def writed(n):
    with open(r'C:\Users\nikita\PycharmProjects\python\practic work\pole_chudes\records.txt', mode='w',
              encoding='UTF8') as r:
        r.write(n)
