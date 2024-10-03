'''
Code Challenge: Solve the Middle Edge in Linear Space Problem.

Input: A match reward, a mismatch penalty, an indel penalty, and two nucleotide strings.
Output: A middle edge in the alignment graph.

Sample Input:
1 1 2
GAGA
GAT

Sample Output:
1 1
2 2
'''

import sys
from typing import List, Dict, Iterable, Tuple
from itertools import chain

# Please do not remove package declarations because these are used by the autograder.

# Insert your MiddleEdge function here, along with any subroutines you need
def MiddleEdge(match_reward: int, mismatch_penalty: int, indel_penalty: int,
                    s: str, t: str) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    #MAKE A MATRIX
    ls = len(s) +1
    lt = len(t)+1
    sm = [[0 for x in range(lt)] for y in range(ls)]
    for i in range(1, ls):
        sm[i][0] = -i*indel_penalty
    for j in range(1, lt):
        sm[0][j] = -j*indel_penalty
    for i in range(1, ls):
          for j in range(1, lt):
            if s[i-1]==t[j-1]:
                  score = match_reward
            else:
                score = -mismatch_penalty
            sm[i][j] = max(sm[i-1][j] - indel_penalty, sm[i][j-1]-indel_penalty, sm[i-1][j-1]+score)
    #print(sm)
    
    #INITALIZE FROM SOURCE:
    midCol = len(t)//2
    fromSource = [[0 for x in range(midCol+1)] for y in range(ls)]
    for i in range(1, ls):
        fromSource[i][0] = -i*indel_penalty
    for j in range(1, midCol+1):
        fromSource[0][j] = -j*indel_penalty
    for i in range(1, ls):
        for j in range(1, midCol+1):
            if s[i-1]==t[j-1]:
                    score = match_reward
            else:
                score = -mismatch_penalty
            fromSource[i][j] = max(fromSource[i-1][j] - indel_penalty, fromSource[i][j-1]-indel_penalty, fromSource[i-1][j-1]+score)

    #INITALIZE FROM SINK
    fromSink = [[0 for x in range(midCol+1)] for y in range(ls)]
    tc = t[midCol:]
    s = s[::-1]
    tc = tc[::-1]
    ltc = len(tc)+1
    fromSink = [[0 for x in range(ltc)] for y in range(ls)]

    for i in range(1, ls):
        fromSink[i][0] = -i*indel_penalty
    for j in range(1, ltc):
        fromSink[0][j] = -j*indel_penalty
    for i in range(1, ls):
        for j in range(1, ltc):
            if s[i-1]==tc[j-1]:
                    score = match_reward
            else:
                score = -mismatch_penalty
            fromSink[i][j] = max(fromSink[i-1][j] - indel_penalty, fromSink[i][j-1]-indel_penalty, fromSink[i-1][j-1]+score)
    reversed_sublists = [sublist[::-1] for sublist in fromSink]
    fromSinkt = list(reversed(reversed_sublists))
    #print(fromSinkt)
    #SUPERIMPOSE AND FIND MIDDLE NODE:
    #now we have fromSource and fromSink, we must iterate thorugh the last column of from Source and the first column of from Sink
    # we can keep track of our best index and our best sum
    bestSum = float('-inf')
    index = None
    for i in range(len(fromSource)):
        num = fromSource[i][-1] + fromSinkt[i][0]
        if num> bestSum:
            bestSum =num
            index = i
    
    middleNode = (index, midCol)
    #print(middleNode)

    #Now you have to find out where your second number came from in fromSink
    #first we go to the index which is [i][0] and we backtrack
    #backtracking refers to seeing what number led up to that, diagonal or right (see if indel= or match or mismatch)
    #remember to stay in indices

    start = fromSinkt[index][0]
    #print("START:",start)
    secondNode= []
    #right side
    if start==(fromSinkt[index][1]-indel_penalty):
        secondNode=[index, midCol+1]
    #top
    elif index>0 and start==fromSinkt[index-1][0]-indel_penalty:
        secondNode = [index-1, midCol+1]
    #top diagonal
    elif index>0 and start== fromSinkt[index-1][1]+match_reward or start== fromSinkt[index-1][1]-mismatch_penalty:
        secondNode=[index-1, midCol+1]
    #bottom diagonal
    elif index<len(s) and start==fromSinkt[index+1][1]+match_reward or start==fromSinkt[index+1][1]+mismatch_penalty:
        secondNode=[index+1, midCol+1]
    #bottom
    elif index<len(s) and start== fromSinkt[index+1][0]-indel_penalty:
        secondNode=[index+1, midCol]

    #print(secondNode)

    second = tuple(secondNode)
    middleE =[middleNode, second]
    middleE = tuple(middleE)
    #print(middleE)
    return middleE