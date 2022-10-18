from math import pi


def a1(n):
    '''

    :param n: параметр
    :return: список градусы минуты секунды
    '''
    # print(f'{int(n)}° {int((n % 1) * 60)}′ {(((n % 1) * 60) % 1) * 60}″')
    return [int(n), int((n % 1) * 60), (((n % 1) * 60) % 1) * 60]


def a2(g, m, s):
    return g + m/60 + s/3600


def a3(n):
    return n * (pi/180)


def a4(n):
    return n * (180/pi)


print(a1(36.97))
print(a2(a1(36.97)[0], a1(36.97)[1], a1(36.97)[2]))
print(a3(36.97))
print(a4(a3(36.97)))
print(help(a1))