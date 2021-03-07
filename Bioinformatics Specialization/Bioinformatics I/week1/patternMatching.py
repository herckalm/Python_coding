"""
Code Challenge: Solve the Pattern Matching Problem.

Input: Two strings, Pattern and Genome.
Output: A collection of space-separated integers specifying all starting
positions where Pattern appears as a substring of Genome.
"""


def pattern_matching(pattern, genome):
    indexes = []
    for i in range(len(genome)):
        if genome.startswith(pattern, i):
            indexes.append(i)
    return indexes


with open('patternMatching.txt') as f:
    text = f.read().splitlines()
f.close()


#indexes = ' '.join(str(c) for c in pattern_matching(text[0], text[1]))
indexes = ' '.join(str(c) for c in pattern_matching("ATA", "GACGATATACGACGATA"))
print(indexes)
