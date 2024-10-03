'''
Code Challenge: Solve the De Bruijn Graph from a String Problem.

Input: An integer k and a string Text.
Output: DeBruijnk(Text), in the form of an adjacency list.

Sample Input:
3
ACGTGTATA

Sample Output:
AC: CG
AT: TA
CG: GT
GT: TA TG
TA: AT
TG: GT
'''

import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your de_bruijn_string function here, along with any subroutines you need
def de_bruijn_string(text: str, k: int) -> Dict[str, List[str]]:
    """Forms the de Bruijn graph of a string."""
    dbList = {}
    length = len(text)
    for i in range(length-k+1):
        l = k-1
        node = text[i:i+l]
        nextk = text[i+1:i+l+1]
        if node in dbList:
            dbList[node].append(nextk)
        else:
            dbList[node] = [nextk]
    return dbList

#the pseudocode for this would be 

'''
DeBruijn Graph from k-mers Problem: Construct the de Bruijn graph from a set of k-mers.

Input: A collection of k-mers Patterns.
Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
Code Challenge: Solve the de Bruijn Graph from k-mers Problem.

Sample Input:
GAGG CAGG GGGG GGGA CAGG AGGG GGAG
Sample Output:
AGG: GGG
CAG: AGG AGG
GAG: AGG
GGA: GAG
GGG: GGA GGG
'''

from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your de_bruijn_kmers function here, along with any subroutines you need
def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    cGraph = {}
    
    for pattern in k_mers:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        if prefix in cGraph:
            cGraph[prefix].append(suffix)
        else:
            cGraph[prefix] = [suffix] 
    return cGraph


