import random


def slova():
    with open(r'slova.txt', encoding='UTF8') as sl:
        return random.choice(sl.read().splitlines()).lower()


def records():
    with open(r'records.txt', mode='r', encoding='UTF8') as r:
        return int(r.read())


def writed(n):
    with open(r'records.txt', mode='w', encoding='UTF8') as r:
        r.write(n)
