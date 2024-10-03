'''
Code Challenge: Use StringReconstruction to solve the String Reconstruction Problem.

Input: An integer k followed by a list of k-mers Patterns.
Output: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)

Sample Input:
3
ACG CGT GTG TGT GTA TAT ATA

Sample Output:ACGTGTATA

'''

import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your string_reconstruction function here, along with any subroutines you need
def string_reconstruction(patterns: List[str], k: int) -> str:
    """Reconstructs a string from its k-mer composition."""
    dB = de_bruijn_kmers(patterns)
    path = eulerian_path(dB)
    Text = PathToGenome(path)
    
    return Text
def de_bruijn_kmers(k_mers: List[str]) -> Dict[str, List[str]]:
    cGraph = {}
    for pattern in k_mers:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        if prefix in cGraph:
            cGraph[prefix].append(suffix)
        else:
            cGraph[prefix] = [suffix] 
    return cGraph

def PathToGenome(path):
    """Forms the genome path formed by a collection of patterns."""
    string = ""
    n= len(path)
    limit = n
    k = len(path[0])
    string +=path[0]
   # i=1
    for i in range(1,limit):
        string += path[i][k-1:]
   # string +=path[-1]
    return string
        

def eulerian_path(g: Dict[int, List[int]]) -> Iterable[int]: 
    graph = g.copy()
    startEnd = findStartEnd(g)
    #print(startEnd)
    start = startEnd[0]
    end = startEnd[1]
    if start==None:
        for node, edge in graph.items():
            if edge:
                start = node
                break
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
    startN = None
    endN=None
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

