'''
Code Challenge: Solve the Local Alignment Problem.

Input: A match reward, a mismatch penalty, an indel penalty, and two nucleotide strings.
Output: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score. 

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

# Insert your LocalAlignment function here, along with any subroutines you need
def LocalAlignment(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                    s: str, t: str) -> Tuple[int, str, str]:
    #so first let's initialize
    ls = len(s) +1
    lt = len(t)+1
    sm = [[0 for x in range(lt)] for y in range(ls)]
    
    #now let's fill in the matrix
    for i in range(1, ls):
          for j in range(1, lt):
            if s[i-1]==t[j-1]:
                  score = match_reward
            else:
                score = -mismatch_penalty
            sm[i][j] = max(sm[i-1][j] - indel_penalty, sm[i][j-1]-indel_penalty, sm[i-1][j-1]+score, 0)    
    
    #now it is traceback time, we want the highest value in the matrix and to traceback from there until the value is about to be 0
    #this is the max in the list
    maxValue = float("-inf")
    indexi =-1
    indexj = -1
    for i in range(ls):
        for j in range(lt):
            if sm[i][j]>maxValue:
                maxValue = sm[i][j]
                indexi = i
                indexj=j
    #now we can traceback and find until it gets to 0
    als = ""
    alt = ""
    i = indexi
    j=indexj
    while sm[i][j]!=0 and i >0 and j>0:
        #so lets first figure out if we got our points from moving diagonal
        if s[i-1]==t[j-1]:
            pscore = sm[i-1][j-1] + match_reward
        else:
            pscore = sm[i-1][j-1] - mismatch_penalty
        if sm[i][j] ==pscore:
            als = s[i-1]+als
            alt = t[j-1]+alt
            i-=1
            j-=1
            continue
        if i>0 and (sm[i][j] ==(sm[i-1][j] - indel_penalty)):
            alt = '-'+alt
            als = s[i-1]+als
            i-=1
        elif sm[i][j] == sm[i][j-1] - indel_penalty:
            alt = t[j-1]+alt
            als = '-'+als
            j-=1

        #als = s[i-1]+als
        #alt = t[j-1]+alt
        #i-=1
        #j-=1
        

    ans = (maxValue, als, alt)
    return ans