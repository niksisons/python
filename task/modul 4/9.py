n = [int(i) for i in input().split()]
if len(set(n)) == 3:
    print(0)
elif len(set(n)) == 2:
    print(2)
else:
    print(3)