'''
Code Challenge: Use OutputLCS (reproduced below) to solve the Longest Common Subsequence Problem.

Input: Two strings s and t.
Output: A longest common subsequence of s and t. (Note: more than one solution may exist, in which case you may output any one.)

Sample Input:
GACT
ATG

Sample Output:
AT

'''

import sys
from typing import List, Dict, Iterable, Tuple
sys.setrecursionlimit(2000) 

# Please do not remove package declarations because these are used by the autograder.

# Insert your LongestCommonSubsequence function here, along with any subroutines you need
def LongestCommonSubsequence(s: str, t: str) -> str:
    matrix = LCSBackTrack(s, t)
    string = OutputLCS(matrix, s, len(s), len(t))
    return string

def LCSBackTrack (v, w):
    lv = len(v)+1
    lw = len(w)+1
    s = [[0 for x in range(lw)] for y in range(lv)]
    Backtrack = [["" for x in range(lw)] for y in range(lv)]
    for i in range(1, lv):
        for j in range(1, lw):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1]+match)
            if s[i][j] == s[i-1][j]:
                Backtrack[i][j] = "|"
            elif s[i][j] == s[i][j-1]:
                Backtrack[i][j] = "-"
            elif s[i][j] == s[i-1][j-1]+match:
                Backtrack[i][j] = "\\"
    
    return Backtrack
                
def OutputLCS(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i][j] == "|":
        return OutputLCS(backtrack, v, i - 1, j)
    elif backtrack[i][j]== "-":
        return OutputLCS(backtrack, v, i, j - 1)
    else:
        return OutputLCS(backtrack, v, i - 1, j - 1) + v[i-1]