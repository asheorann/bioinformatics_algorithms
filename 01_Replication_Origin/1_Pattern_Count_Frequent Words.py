import sys

# Please do not remove package declarations because these are used by the autograder.
# Insert your PatternCount function here, along with any subroutines you need

#Input: Strings Text and Pattern.
#Output: Count(Text, Pattern).

def pattern_count(text: str, pattern: str) -> int:
    length = len(text)-1
    plength = len(pattern)
    count = 0
    for i in range(length):
        if text[i:i+plength] == pattern:
            count +=1
    return count

#Input: A string Text and an integer k.
#Output: All most frequent k-mers in Text.

# Please do not remove package declarations because these are used by the autograder.

# Insert your frequent_words function here, along with any subroutines you need
def frequent_words(text: str, k: int) -> list[str]:
    """Find the most frequent k-mers in a given text."""
    frequentPatterns = []
    freqMap = {}
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        if pattern in freqMap:
            freqMap[pattern]+=1
        else:
            freqMap[pattern] = 1
    maxValue = max(freqMap.values())
    for p, v in zip(freqMap.keys(), freqMap.values()):
        if v == maxValue:
            frequentPatterns.append(p)
    return frequentPatterns
