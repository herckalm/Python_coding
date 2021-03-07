"""
Reverse Complement Problem: Find the reverse complement of a DNA string.

Input: A DNA string Pattern.
Output: The reverse complement of Pattern.
"""


def reverse_pattern(dna):
    reverse_dna = ""
    for nucleotide in dna:
        if nucleotide == "A":
            reverse_dna += "T"
        elif nucleotide == "T":
            reverse_dna += "A"
        elif nucleotide == "C":
            reverse_dna += "G"
        elif nucleotide == "G":
            reverse_dna += "C"
    return reverse_dna[::-1]


with open('reverseString.txt') as f:
    text = f.read()
f.close()

#print(reverse_pattern(text))

print(reverse_pattern("TTGTGTC"))
