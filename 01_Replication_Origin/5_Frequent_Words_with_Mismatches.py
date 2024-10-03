'''
Code Challenge: Solve the Frequent Words with Mismatches Problem.

Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
Output: All most frequent k-mers with up to d mismatches in Text.

Sample Input:
ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1
Sample Output: ATGT GATG ATGC
'''

import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your frequent_words_with_mismatches function here, along with any subroutines you need
def frequent_words_with_mismatches(text: str, k: int, d: int) -> list[str]:
    """Find the most frequent k-mers with up to d mismatches in a text."""
    patterns = []
    freqMap = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i: i+k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
           # neighbor = neighborhood[j]
            if neighbor not in freqMap:
                freqMap[neighbor] =1
            else:
                freqMap[neighbor]+=1
    m = max(freqMap.values())
    for pattern in freqMap:
        if freqMap[pattern] == m:
            patterns.append(pattern)
    return patterns
               
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    count = 0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count+=1
    return count

def neighbors(s: str, d: int) -> list[str]:
    """Generate neighbors of a string within a given Hamming distance."""
    neighborhood= set()
    if d == 0:
        return {s}
    if len(s)==1:
        return {'A', 'C', 'G', 'T'}
    suffixNeighbors = neighbors(s[1:], d)
    for i in suffixNeighbors:
        if hamming_distance(s[1:], i)<d:
            for j in {'A', 'C', 'G', 'T'}:
                neighborhood.add(j+i)
        else:
            neighborhood.add(s[0]+i)
    return neighborhood