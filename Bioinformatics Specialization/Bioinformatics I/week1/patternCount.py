"""
Code Challenge: Implement patternCount.
     Input: Strings Text and Pattern.
     Output: Count(Text, Pattern).

     patternCount(Text, Pattern)
        count ← 0
        for i ← 0 to |Text| − |Pattern|
            if Text(i, |Pattern|) = Pattern
            count ← count + 1
        return count
"""


def pattern_count(text, pattern):
    count = 0
    loop_range = len(text) - len(pattern)
    for i in range(loop_range + 1):
        if text[i:len(pattern) + i] == pattern:
            count += 1
    return count


with open('patternCount.txt') as f:
    text = f.read()
f.close()

print(pattern_count(text, "CGCCGACCG"))