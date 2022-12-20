def first_non_repeating_letter(st):
    low = st.lower()
    for i in range(len(low)):
        if low.count(low[i]) == 1:
            return st[i]
    else:
        return ''


# print(first_non_repeating_letter('SSTt'))

n ={'1': 1, '2': 2, '3': 3}
print(sorted(n, reverse=True))

