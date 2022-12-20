import random
import string


def main():
    alpha_low = string.ascii_lowercase
    alpha_upp = string.ascii_uppercase
    digit = string.digits
    pun = string.punctuation
    count = int(input('Введите количество паролей: '))
    lening = int(input('Ведите длину пароля: '))
    opcen = (input('Введите из чего будет состоять пароль(0.А, 1.а, 2.\, 3.0): '))
    sp_values = []
    str_values = ''
    if len(opcen) != 0:
        if '0' in opcen:
            sp_values.append(alpha_upp)
            str_values += alpha_upp
        if '1' in opcen:
            sp_values.append(alpha_low)
            str_values += alpha_low
        if '2' in opcen:
            sp_values.append(pun)
            str_values += pun
        if '3' in opcen:
            sp_values.append(digit)
            str_values += digit
    else:
        sp_values = [alpha_upp, alpha_low, digit, pun]
        str_values = alpha_upp + alpha_low + digit + pun
    for p in range(count):
        sp_values = sp_values
        str_values = str_values
        password = ''
        for i in range(lening):
            if len(sp_values) != 0:
                vl = random.choice(sp_values)
                password += random.choice(vl)
                sp_values.remove(vl)
            else:
                password += random.choice(str_values)
        writen(password + '\n')


def writen(n):
    with open('pass', 'a', encoding='utf8') as f:
        f.write(n)


main()
