import requests as rq
#
#
# rez = rq.get('https://stepic.org/media/attachments/course67/3.6.2/555.txt')
# print(len(list(rez.text.strip().splitlines())))
#
# rez = rq.get('https://stepic.org/media/attachments/course67/3.6.2/555.txt')
# print(rez.text)

#

link1 = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
while True:
    end_date = rq.get(link1).text
    print(end_date)
    if end_date[0] == 'W' and end_date[1] == 'e':
        print(end_date)
        break
    else:
        link1 = 'https://stepic.org/media/attachments/course67/3.6.3/' + end_date
