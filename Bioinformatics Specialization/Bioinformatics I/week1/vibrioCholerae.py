"""
Return a space-separated list of starting positions (in increasing order)
where CTTGATCAT appears as a substring in the Vibrio cholerae genome.
"""


def vibrio_cholerae(pattern, genome):
    indexes = []
    for i in range(len(genome)):
        if genome.startswith(pattern, i):
            indexes.append(i)
    return indexes


with open('vibrioCholerae.txt') as f:
    text = f.read()
f.close()


print(vibrio_cholerae("CTTGATCAT", text))
