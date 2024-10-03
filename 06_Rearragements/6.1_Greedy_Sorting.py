'''
Code Challenge: Implement GreedySorting (reproduced below).

Input: A permutation P.
Output: The sequence of permutations corresponding to applying GreedySorting to P, ending with the identity permutation.

Sample Input:
-3 +4 +1 +5 -2

Sample Output:
-1 -4 +3 +5 -2
+1 -4 +3 +5 -2
+1 +2 -5 -3 +4
+1 +2 +3 +5 +4
+1 +2 +3 -4 -5
+1 +2 +3 +4 -5
+1 +2 +3 +4 +5
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your GreedySorting function here, along with any subroutines you need
def GreedySorting(P: List[int]) -> List[List[int]]:
    permutations =[]
    k=0
    count =0
    for k in range(len(P)):
        if P[k]!=(k+1):
           # print("entered")
            if (k+1) in P:
                to = P.index(k+1)
                #print(to)
            elif -(k+1) in P:
                to = P.index(-(k+1))
            
            r = reversal(k, to, P)
            P=r
            permutations.append(r)
            count+=1
        if P[k]==(-(k+1)):
         #   print("second if")
            r = reversal(k,k,P)
            P=r
            permutations.append(r)
            count+=1
    
    #P=[1, -2, 3]
    #r = reversal(1,1,P)
    #permutations.append(r)
    #print(count)
    return permutations

def reversal(k, to, P):
    Q = P.copy()
    part = Q[k:to+1]
    #print(part)
    part.reverse()
    Q[k:to+1]=part
    i = k
    #print(i)
    for i in range(k, to+1):
        Q[i] = -(Q[i])
    return Q