'''
Code Challenge: Solve the Eulerian Path Problem.

Input: The adjacency list of a directed graph that has an Eulerian path.
Output: An Eulerian path in this graph.

Sample Input:
0: 2
1: 3
2: 1
3: 0 4
6: 3 7
7: 8
8: 9
9: 6

Sample Output:
6 7 8 9 6 3 0 2 1 3 4
'''

import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your eulerian_path function here, along with any subroutines you need
# g[u] is the list of neighbors of the vertex u

def eulerian_path(g: Dict[int, List[int]]) -> Iterable[int]: 
    graph = g.copy()
    startEnd = findStartEnd(g)
    #print(startEnd)
    start = startEnd[0]
    end = startEnd[1]
    path = [start]
    visited = [] 
    curr = start
    solution = []
    #print(curr)
   # nextn = graph[curr][0]
    while any(graph.values()):
        curr = path[-1]
        if curr in graph and graph[curr]:
            nextn = graph[curr].pop()
            path.append(nextn)
        else:                  
            add = path.pop()
            solution.append(add)
           # latest = path[-1]      
           # if visited.count(nextn)<5:
               #     visited.append(nextn)
                 #   graph[latest] = [nextn] + graph[latest]
    path= path[::-1]
    solution = solution + path
    solution = solution[::-1]
   
    
    return solution
def findStartEnd(g: Dict[int, list[int]])->list[int]:
    startEnd = []
    edgesList = []
    #endN=None
    nodes= list(g.keys())
    for edge in g.values():
            edgesList.extend(edge)
    allNodes = edgesList+nodes
    allNodes = set(allNodes)
    degrees = {}
    for edge in allNodes:
        inDegree = edgesList.count(edge)
        degrees[edge] = [inDegree]
        if edge in g:
            outDegree = len(g[edge])
            degrees[edge].append(outDegree)
        else:
            outDegree = 0
            degrees[edge].append(outDegree)
        diff = degrees[edge][0]-degrees[edge][1]

        if diff<0:
            startN = edge
        if diff> 0:
            endN = edge
    startEnd.append(startN)
    startEnd.append(endN)
    return startEnd
