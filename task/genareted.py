import random

for i in range(10001):
    a = [0, 0, 1]
    b = random.choice(a)
    a.remove(b)
