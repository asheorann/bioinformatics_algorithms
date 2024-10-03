'''
Implement MotifEnumeration (reproduced below).

Input: Integers k and d, followed by a space-separated collection of strings Dna.
Output: All (k, d)-motifs in Dna.

Sample Input: 3 1
ATTTGGC TGCCTTA CGGTATC GAAAATT
Sample Output:TTT ATT GTT ATA
'''

import sys

# Please do not remove package declarations because these are used by the autograder.

# Insert your motif_enumeration function here, along with any subroutines you need
def motif_enumeration(dna: list[str], k: int, d: int) -> list[str]:
    """Implements the MotifEnumeration algorithm."""
    patterns = set()
    length = len(dna[0])
    for i in range (length-k+1):
        # for j in range(length-k+1):
        pattern = dna[0][i:i+k]
        nList = neighbors(pattern, d)
        for n in nList:
            # if it appears in all the different strings
            #then we add it to patters
            if inAllStrings(dna, n, d)==True:
                patterns.add(n)
    return list(patterns)

def inAllStrings(dna: list[str], pattern: str, d: int) -> bool:
    for i in range(len(dna)):
        length = len(dna[i])
        found = False
        l = len(pattern)
        for j in range(length-l+1):
            if hamming_distance(pattern, dna[i][j:j+len(pattern)])<=d:
                found = True
                break
        if found==False:
            return False
    return True
        

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