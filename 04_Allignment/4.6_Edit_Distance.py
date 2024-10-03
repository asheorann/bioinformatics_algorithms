'''
Edit Distance Problem: Find the edit distance between two strings.

Input: Two strings.
Output: The edit distance between these strings.

Sample Input:
GAGA
GAT

Sample Output:2
'''
import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your EditDistance function here, along with any subroutines you need
def EditDistance(s: str, t: str) -> int:
    ls = len(s) +1
    lt = len(t)+1
    
    #INITIALIZED!
    sm = [[0 for x in range(lt)] for y in range(ls)]
    for i in range(1, ls):
        sm[i][0] = i
    for j in range(1, lt):
        sm[0][j] = j
    
    #now lets fill it in
    for i in range(1, ls):
        for j in range(1, lt):
            up = sm[i-1][j]
            left = sm[i][j-1]
            diag = sm[i-1][j-1]
            minNum = min(up, left, diag)           
            if s[i-1]==t[j-1]:
                add = sm[i-1][j-1]
            else:
                add = minNum+1
            sm[i][j] = add
    #now let us extract the final answer
    editDist = sm[-1][-1]
    
    return editDist
