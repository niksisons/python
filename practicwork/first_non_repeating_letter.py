def first_non_repeating_letter(st):
    low = st.lower()
    for i in range(len(low)):
        if low.count(low[i]) == 1:
            return st[i]
    else:
        return ''


print(first_non_repeating_letter('SSTt'))

