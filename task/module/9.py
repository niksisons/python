a = int(input())
if a % 60 < 10:
    print(a // 60, ':0', a % 60, sep='')
else:
    print(a // 60, ':', a % 60, sep='')