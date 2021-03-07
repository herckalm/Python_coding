"""
Code Challenge: Solve the Frequent Words Problem.
Input: A string Text and an integer k.
Output: All most frequent k-mers in Text.

FrequencyTable(Text, k) (function is placed in commonFunctions.py)
    freqMap ← empty map
    n ← |Text|
    for i ← 0 to n − k
        Pattern ← Text(i, k)
        if freqMap[Pattern] doesn't exist
            freqMap[Pattern]← 1
        else
           freqMap[pattern] ←freqMap[pattern]+1
    return freqMap

FrequentPatterns(Text, k)
    Patterns ← an array of strings of length 0
    freqMap ← FrequencyTable(Text, k)
    max ← MaxMap(freqMap)
    for all strings Pattern in freqMap
        if freqMap[pattern] = max
            append Pattern to Patterns
    return Patterns
"""


from commonFunctions import frequency_table


def frequent_patterns(text, k):
    patterns = []
    frequency_map = frequency_table(text, k)
    max_value = max(frequency_map.values())
    for key in frequency_map.keys():
        if frequency_map[key] == max_value:
            patterns.append(key)

    return patterns


with open('frequentWords.txt') as f:
    text = f.read()
f.close()

print(frequent_patterns(text, 12))

#print(frequent_patterns("TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT", 3))
