'''
Code Challenge: Solve the Eulerian Cycle Problem.

Input: The adjacency list of an Eulerian directed graph.
Output: An Eulerian cycle in this graph.

Sample Input:
0: 3
1: 0
2: 1 6
3: 2
4: 2
5: 4
6: 5 8
7: 9
8: 7
9: 6

Sample Output: 0 3 2 6 8 7 9 6 5 4 2 1 0
'''

import sys
from typing import List, Dict, Iterable

def eulerian_cycle(g: Dict[int, List[int]]) -> Iterable[int]:
    graph  = g.copy()
    iCycle = []
    start = None

    for node, edge in graph.items():
        if edge:
            start = node
            break
    if start is None:
        return iCycle
    curr = start
    iCycle.append(curr)
    visited =0
    maxVisit = maxVisits(graph)
    
    while visited<=maxVisit:

        nextn = graph[curr][0]
        while nextn!=start or (nextn in graph[start]):

            if len(graph[curr])==0:
                del graph[curr]
                curr= nextn

            elif len(graph[curr])>0:
                nextn = graph[curr].pop(0)
                iCycle.append(nextn)

                curr = nextn  

        if nextn == start:
                nStart = 0
                l = len(iCycle)

                while nStart<l:
                    if len(graph[iCycle[nStart]])!=0 and (nStart+1)!=start:
                        break
                    nStart+=1 
                    
                if nStart < len(iCycle):
                    nCycle = iCycle[nStart:] +iCycle[1:nStart+1]
                    iCycle=nCycle
                    curr = iCycle[-1]
                    start = curr
                    visited=len(iCycle)
                  
                else:
                    break

    return iCycle
def maxVisits(graph: Dict[int, list[int]]):
    totalOut = sum(len(edges) for edges in graph.values())
    print("maxVisits", totalOut)
    return totalOut

    