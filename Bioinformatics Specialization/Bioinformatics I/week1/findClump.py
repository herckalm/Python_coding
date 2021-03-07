"""
Code Challenge: Solve the Clump Finding Problem.
You will need to make sure that your algorithm is efficient enough to handle a large dataset.

Clump Finding Problem: Find patterns forming clumps in a string.

Input: A string Genome, and integers k, L, and t.
Output: All distinct k-mers forming (L, t)-clumps in Genome.

FindClumps(Text, k, L, t)
    Patterns ← an array of strings of length 0
    n ← |Text|
    for every integer i between 0 and n − L
        Window ← Text(i, L)
        freqMap ← FrequencyTable(Window, k)
        for every key s in freqMap
            if freqMap[s] ≥ t
                append s to Patterns
    remove duplicates from Patterns
    return Patterns
"""
from commonFunctions import frequency_table


def find_clump(text, k, l, t):
    patterns = []
    n = len(text)
    genome_map = {}
    loop_range = n-l
    for i in range(loop_range+1):
        window = text[i:l+i]
        genome_map = frequency_table(window, k)
        for key, value in genome_map.items():
            if value >= t:
                patterns.append(key)
    return len(set(patterns))


with open('findClump.txt') as f:
    text = f.read().splitlines()
f.close()

(k, l, t) = (10, 28, 4)


result = find_clump(text, k, l, t)

if result == 0:
    print("There aren't exist such k-mers")
else:
    print(result)

