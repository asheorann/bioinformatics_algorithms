'''
Code Challenge: Solve the String Spelled by a Genome Path Problem.

Input: A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).

Sample Input:
ACCGA CCGAA CGAAG GAAGC AAGCT
Sample Output:
ACCGAAGCT
'''

import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your genome_path function here, along with any subroutines you need
def genome_path(path: List[str]) -> str:
    """Forms the genome path formed by a collection of patterns."""
    string = ""
    n= len(path)
    limit = n
    k = len(path[0])
    string +=path[0]
   # i=1
    for i in range(1,limit):
        string += path[i][k-1:]
    return string

'''
Code Challenge: Solve the Overlap Graph Problem (restated below).

Input: A collection Patterns of k-mers.
Output: The overlap graph Overlap(Patterns),
in the form of an adjacency list. (You may return the nodes and their edges in any order.)

Sample Input:

AAG AGA ATT CTA CTC GAT TAC TCT TCT TTC
Sample Output:

AAG: AGA
AGA: GAT
ATT: TTC
CTA: TAC
CTC: TCT
GAT: ATT
TCT: CTA CTC
TTC: TCT
'''

from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your overlap_graph function here, along with any subroutines you need
def overlap_graph(patterns: List[str]) -> Dict[str, List[str]]:
    """Forms the overlap graph of a collection of patterns."""
    n = len(patterns)
    k = len(patterns[0])
    #adj_matrix = [[0 for x in range(n)] for x in range(n)]
    neighbors = {}
    for i in range(n):
        suf = suffix(patterns[i])
        neighbors[patterns[i]] = set()
        for j in range(n):
           # if i!=j:
                pre = prefix(patterns[j])
                if suf==pre:
                    neighbors[patterns[i]].add(patterns[j])
   # aList = makeList(patterns, adj_matrix)
    #return aList
    aList ={}
    for key, value in neighbors.items():
        if value:
            aList[key] = sorted(list(value))
   # aList = {key: sorted(list(value)) for key, value in neighbors.items() if value
    return aList
        
def suffix(pattern: str):
    k = len(pattern)
    if k >= 2:
        suf = pattern[1:k]
        return suf
    return ""
def prefix(pattern: str):
    k = len(pattern)
    if k >= 2:
        pre = pattern[0:k-1]
        return pre
    return ""
