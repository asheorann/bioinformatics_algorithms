'''
Code Challenge: Solve the 2-Break Distance Problem.

Input: Genomes P and Q.
Output: The 2-break distance d(P, Q).

Sample Input:
(+1 +2 +3 +4 +5 +6)
(+1 -3 -6 -5)(+2 -4)

Sample Output: 3
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your TwoBreakDistance function here, along with any subroutines you need
def TwoBreakDistance(P: List[List[int]], Q: List[List[int]]) -> int:
    #genome is turned
    blockNumber=NumberBlocks(P, Q)
   # print(blockNumber)
    cNumber = CycleNumber(P,Q)
    d = blockNumber-cNumber
    return d

def CycleNumber(P: List[List[int]], Q: List[List[int]]) -> int:
    #create the list of edges
    cycleP= ColoredEdges(P)
    cyclePL= [list(edge) for edge in cycleP]
    cycleQ=ColoredEdges(Q)
    cycleQL= [list(edge) for edge in cycleQ]
    
    cycleCount=0
    while cyclePL and cycleQL:
        start = cyclePL[0][0]
        curr = cyclePL[0][1]
        index = 0
        indexj=0
        cyclePL.pop(0)
        while curr!=start: 
            for i in range(len(cycleQ)):
                if cycleQL[i][0]==curr:
                    curr =cycleQL[i][1]
                    index=i
                    break
                elif cycleQL[i][1]==curr:
                    curr =cycleQL[i][0]
                    index=i
                    break
            cycleQL.pop(index)
            for j,edge in enumerate(cyclePL):
                if edge[0]==curr:
                    curr = edge[1]
                    cyclePL.pop(j)
                    break
                elif edge[1] == curr:
                    curr = edge[0]
                    cyclePL.pop(j)
                    break
            #cyclePL.pop(indexj)
        cycleCount+=1
           
    return cycleCount
    
def NumberBlocks(P: List[List[int]], Q: List[List[int]]):
    blocks = []
    for i in range(len(P)):
        for j in range(len(P[i])):
            blocks.append(P[i][j])
    blocks = set(blocks)
    number = len(blocks)
    return number
    
    
def ColoredEdges(P: List[List[int]]) -> List[Tuple[int, int]]:
    edges = []
    for chromosome in P:
        nodes = ChromosomeToCycle(chromosome)
        n = len(nodes)
        for i in range(1,n,2):
            if  i==(n-1):
                edge = (nodes[n-1], nodes[0])
                edges.append(edge)
                break
            else:
                edge = (nodes[i], nodes[i+1])
                edges.append(edge)
    return edges  
                       
def ChromosomeToCycle(Chromosome: List[int]) -> List[int]:
    output = []

    for i in range(len(Chromosome)):
        j = (abs(Chromosome[i])-1)*2+1
        if Chromosome[i]>0:
            output.append(j)
            output.append(j+1)
        else:
            output.append(j+1)
            output.append(j)
    return output