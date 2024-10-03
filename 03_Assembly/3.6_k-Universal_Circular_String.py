'''
Code Challenge: Solve the k-Universal Circular String Problem.

Input: An integer k.
Output: A k-universal circular string.
Sample Input:
3
Sample Output:00010111
'''

import sys
from typing import List, Dict, Iterable

# Please do not remove package declarations because these are used by the autograder.

# Insert your k_universal_string function here, along with any subroutines you need
def k_universal_string(k: int) -> str:
    """Generates a k-universal circular string."""
    array = [0]*k
    i=0
    k_mers= listCreate(k, array, i)
    dB = de_bruijn_kmers(k_mers)
    #print("db:", dB)
    path = eulerian_cycle(dB)
   # print("cycle:", path)
    #path = list(set(path))
    string = PathToGenome(path)
    return string

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
    string = ""
    n= len(path)
    limit = n
    k = len(path[0])
    string +=path[0]
   # i=1
    for i in range(1,limit):
        string += path[i][k-1:]
    return string
        

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
    #print(iCycle)
    while graph:
        if curr in graph and graph[curr]:
            nextn = graph[curr].pop(0)
            iCycle.append(nextn)
            curr = nextn
        else:
            iCycle.pop()
            curr = iCycle[-1]
        rGraph = {}
        for key, value in graph.items():
            if value:
                rGraph[key] = value
        #print(rGraph)
        graph = rGraph

        
    return iCycle
def maxVisits(graph: Dict[int, list[int]]):
    totalOut = sum(len(edges) for edges in graph.values())
    #print("maxVisits", totalOut)
    return totalOut
def listCreate(k, array, i):
    listBinary = []
    def stringCreate(i): 
        if i == k:
            add = array.copy()
            listBinary.append(add)
            return
        array[i] = 0
        stringCreate(i+1)
        array[i] = 1
        stringCreate(i+1)
    stringCreate(0)
    binaryL = []
    for binary in listBinary:
        bString = ""
        for num in binary:
            bString+=str(num)
        binaryL.append(bString)
    return binaryL