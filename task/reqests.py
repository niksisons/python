import requests as rq


rez = rq.get('https://stepic.org/media/attachments/course67/3.6.2/555.txt')
print(len(list(rez.text.strip().splitlines())))

rez = rq.get('https://stepic.org/media/attachments/course67/3.6.2/555.txt')
print(rez.text)