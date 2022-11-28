from math import pi


def a1(n: float) -> list:
    '''
    :param n: Вещественное число.
    :return: список градусы минуты секунды.
    '''
    # print(f'{int(n)}° {int((n % 1) * 60)}′ {(((n % 1) * 60) % 1) * 60}″')
    return [int(n), '° ', int((n % 1) * 60), '′ ', (((n % 1) * 60) % 1) * 60, '″']


def a2(g: float, m: float, s: float) -> float:
    '''
    :param g: Градусы.
    :param m: Минуты.
    :param s: Секунды.
    :return: Вещественное число.
    '''
    return g + m/60 + s/3600


def a3(n: float) -> float:
    '''
    :param n: Вещественное число.
    :return: не помню.
    '''
    return n * (pi/180)


def a4(n: float) -> float:
    '''
    :param n: тоже не помню.
    :return: Вещественное число.
    '''
    return n * (180/pi)


if __name__ == '__main__':
    print(''.join(map(str, a1(36.97))))
    print(a2(a1(36.97)[0], a1(36.97)[2], a1(36.97)[4]))
    print(a3(36.97))
    print(a4(a3(36.97)))
# print(help())