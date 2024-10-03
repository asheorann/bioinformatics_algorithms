#Hamming Distance Problem: Compute the Hamming distance between two strings.

#Input: Two strings of equal length.
#Output: The Hamming distance between these strings.

#Sample Input 1:
#GGGCCGTTGGT
#GGACCGTTGAC
#Sample Output 1:3

import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your hamming_distance function here, along with any subroutines you need
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    count = 0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count+=1
    return count
'''
Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

Input: Strings Pattern and Text along with an integer d.
Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
Sample Input:
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
3
Sample Output: 6 7 26 27

'''
def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    count = 0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count+=1
    return count

def approximate_pattern_matching(pattern: str, text: str, d: int) -> list[int]:
    """Find all starting positions where Pattern appears as a substring of Text with at most d mismatches."""
    length = len(text)
    plength = len(pattern)
    starts = []
    for i in range(length-plength+1):
        subs= text[i:i+plength]
        if subs == pattern:
            starts.append(i)
        elif (hamming_distance(subs, pattern)<=d):
            starts.append(i)
    return starts

'''
Code Challenge: Implement ApproximatePatternCount.

Input: Strings Pattern and Text as well as an integer d.
Output: Countd(Text, Pattern).

Sample Input:
GAGG
TTTAGAGCCTTCAGAGG
2
Sample Output: 4
'''
def approximate_pattern_count(text: str, pattern: str, d: int) -> int:
    """Count the occurrences of a pattern in a text, allowing for up to d mismatches."""
    length = len(text)
    plength = len(pattern)
    count = 0
    for i in range(length-plength+1):
        subs= text[i:i+plength]
        if subs == pattern:
            count +=1
        elif (hamming_distance(subs, pattern)<=d):
            count +=1
    return count
