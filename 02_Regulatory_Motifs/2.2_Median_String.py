'''
Code Challenge: Implement MedianString.

Input: An integer k, followed by a space-separated collection of strings Dna.
Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all possible choices of k-mers. (If there are multiple such strings Pattern, then you may return any one.)

Sample Input:
3
AAATTGACGCAT GACGACCACGTT CGTCAGCGCCTG GCTGAGCACCGG AGTACGGGACAG
Sample Output:ACG
'''

import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your median_string function here, along with any subroutines you need

def median_string(dna: list[str], k: int) -> str:
    """Identifies the median string of length k in a collection of longer strings."""
    distance = float('inf')
    median = ""
   # l = len(dna[0])

    for i in range(4**k):
        # first i want to put pattern
        pattern= np(i,k)
        if distance> d(pattern,dna):
            distance = d(pattern, dna)
            median = pattern
    return median

def np(i, k):
    pattern = ""
    m = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

    while k > 0:
        k -= 1
        q = i//4
        r = i%4
        pattern = pattern+m[r]
        i = q

    return pattern

def d(pattern, dna):
    length = len(pattern)  
    distance = 0
    for string in dna:
        distance +=mhamming_distance(pattern, string)
    return distance

def mhamming_distance(pattern, string):
    
    add = float('inf')
    plength = len(pattern)
    
    length = len(string)
    for i in range(length-plength+1):
        seq = string[i:i+plength]
        distance = hamming_distance(pattern, seq)
        add = min(add, distance)
    return add



def hamming_distance(p: str, q: str) -> int:
    """Calculate the Hamming distance between two strings."""
    count = 0
    for i in range(len(p)):
        if p[i]!=q[i]:
            count+=1
    return count