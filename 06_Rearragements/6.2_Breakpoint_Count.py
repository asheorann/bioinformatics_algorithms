'''
Number of Breakpoints Problem: Find the number of breakpoints in a permutation.

Input: A permutation.
Output: The number of breakpoints in this permutation.

Sample Input:
+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14

Sample Output: 8
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your BreakpointCount function here, along with any subroutines you need
def BreakpointCount(P: List[int]) -> int:
    count =0
    for i in range(len(P)-1):
        if P[i+1]!=P[i]+1:
            count+=1
    n=len(P)
    if P[0]!=1:
        count+=1
    if P[-1]!=n:
        count+=1
    return count
       