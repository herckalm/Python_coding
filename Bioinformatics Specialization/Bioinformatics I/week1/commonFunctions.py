def frequency_table(text, k):
    frequency_dict = {}
    n = len(text)
    for i in range(n-k):
        pattern = text[i:k+i]
        if pattern in frequency_dict.keys():
            frequency_dict[pattern] += 1
        else:
            frequency_dict[pattern] = 1
    return frequency_dict
