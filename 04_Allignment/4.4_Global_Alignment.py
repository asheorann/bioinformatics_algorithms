'''
Code Challenge: Solve the Global Alignment Problem.

Input: A match reward, a mismatch penalty, an indel penalty, and two nucleotide strings.
Output: The maximum alignment score of these strings followed by an alignment achieving this maximum score.

Sample Input:
1 1 2
GAGA
GAT

Sample Output:
-1
GAGA
GA-T
'''

import sys
from typing import List, Dict, Iterable, Tuple
sys.setrecursionlimit(2000) 
# Please do not remove package declarations because these are used by the autograder.

# Insert your GlobalAlignment function here, along with any subroutines you need
def GlobalAlignment(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                    s: str, t: str) -> Tuple[int, str, str]:
    ls = len(s) +1
    lt = len(t)+1
    #changed
    sm = [[0 for x in range(ls)] for y in range(lt)]
    backtrack = [["" for a in range(ls)] for b in range(lt)]
    for i in range(1, lt):
        sm[i][0] = -i*indel_penalty
    for j in range(1, ls):
        sm[0][j] = -j*indel_penalty
    #count =0
    for i in range(1, lt):
          for j in range(1, ls):
            if t[i-1]==s[j-1]:
                  score = match_reward
            else:
                score = -mismatch_penalty
            sm[i][j] = max(sm[i-1][j] - indel_penalty, sm[i][j-1]-indel_penalty, sm[i-1][j-1]+score)
    als = ""
    alt = ""
    i = len(t)
    j = len(s)
    while i>0 or  j>0:
        if i>0 and j>0:
            if s[j-1] ==t[i-1]:
                pscore = sm[i-1][j-1] + match_reward
            else:
                pscore = sm[i-1][j-1] - mismatch_penalty
            if sm[i][j] ==pscore:
                als = s[j-1]+als
                alt = t[i-1]+alt
                i-=1
                j-=1
                continue

                
        if i>0 and (j==0 or (sm[i][j] ==(sm[i-1][j] - indel_penalty))):
            als = '-'+als
            alt = t[i-1]+alt
            i-=1
        elif j>0:
            als = s[j-1]+als
            alt = '-'+alt
            j-=1
    #print(sm)
    l= len(als)
    return (l, sm[-1][-1], als, alt)
