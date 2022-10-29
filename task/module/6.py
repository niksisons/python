n = int(input())
print(n // 3600 and n // 60 if (n // 3600) < 24 and (n // 60) < 1339 else (n // 3600) % 24, (n // 60) % 1339)
