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

I didn't follow the above pseudocode exactly here
in order to accommodate with large genome data (eColi.txt)
"""


def find_clump(text, k, l, t):
    genome_map = {}
    for i in range(l):
        window = text[i:k+i]
        genome_map[window] = genome_map.get(window, 0) + 1
    clump = [key for key, value in genome_map.items() if value >= t]
    for i in range(1, len(text) - l + 1):
        first_pattern = text[(i - 1):(i - 1 + k)]
        genome_map[first_pattern] -= 1
        last_pattern = text[(i + l - k):(i + l)]
        genome_map[last_pattern] = genome_map.get(last_pattern, 0) + 1
        if genome_map[last_pattern] >= t and last_pattern not in clump:
            clump.append(last_pattern)
    return clump


with open('eColi.txt') as f:
    text = f.read()
f.close()
(k, l, t) = (9, 500, 3)

result = len(find_clump(text, k, l, t))

if result == 0:
    print("There aren't exist such k-mers")
else:
    print(result)

