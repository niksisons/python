n = int(input())
input_data = [input().split(';') for i in range(n)]
print(input_data)
output_data = []
for i in input_data:
    for j in range(0, len(i), 2):
        peremennay_str = i[j]
        if i[1] > i[-1]:
            peremennay_str +=
        if i[1] == i[-1]:

        else:
            output_data[i[j]] += 1
print(output_data)


