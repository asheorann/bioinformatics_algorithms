'''
Code Challenge: Solve the Overlap Alignment Problem.

Input: A match reward, a mismatch penalty, an indel penalty, and two nucleotide strings v and w.
Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of v and a prefix w' of w achieving this maximum score.

Sample Input:
1 1 2
GAGA
GAT

Sample Output:
2
GA
GA
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your OverlapAlignment function here, along with any subroutines you need
def OverlapAlignment(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                    s: str, t: str) -> Tuple[int, str, str]:
    ls = len(s) +1
    lt = len(t)+1
    sm = [[0 for x in range(lt)] for y in range(ls)]
    for j in range(1, lt):
        sm[0][j] = -j*indel_penalty

    #fill in matrix
    for i in range(1, ls):
          for j in range(1, lt):
            if s[i-1]==t[j-1]:
                  score = match_reward
            else:
                score = -mismatch_penalty
            sm[i][j] = max(sm[i][j-1]-indel_penalty, sm[i-1][j]-indel_penalty, sm[i-1][j-1]+score)    
    
    #this is the max in the list
    maxValue = max(sm[-1])
    indexj = sm[-1].index(maxValue)
    indexi =ls-1
    #now we can traceback and find until it gets to the start of the line
    als = ""
    alt = ""
    i = indexi
    j=indexj
    while j>0 and i>0:
        if s[i-1] == t[j-1]:
            curr = sm[i][j]
            diag = sm[i-1][j-1]+match_reward
            if curr == diag:
                als = s[i - 1] + als
                alt = t[j - 1] + alt
                i -= 1
                j -= 1
                continue
        elif sm[i][j] == sm[i-1][j-1] - mismatch_penalty:
            als = s[i - 1] + als
            alt = t[j - 1] + alt
            i -= 1
            j -= 1
            continue
            
        if (sm[i][j] ==(sm[i][j-1]- indel_penalty)):
            alt = t[j-1]+alt
            als = '-'+als
            j-=1
        elif (sm[i][j] ==(sm[i-1][j]- indel_penalty)):
            alt = '-'+alt
            als = s[i-1]+als
            i-=1
      #  else:
       #     alt = t[j - 1] + alt
        #    als = s[i-1] + als
         #   i -= 1
          #  j -= 1  
           # sm[i][j] -= mismatch_penalty
    if j > 0:
        alt = t[:j] + alt
        als = '-' * j + als
    ans = (maxValue, als, alt)
    return ans