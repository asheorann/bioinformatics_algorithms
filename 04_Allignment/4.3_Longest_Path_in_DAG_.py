'''
Code Challenge: Solve the Longest Path in a DAG Problem.

Input: An integer representing the starting node to consider in a graph, followed by an integer representing the ending node to consider, followed by a list of edges in the graph. The edge notation "0 1 7" indicates that an edge connects node 0 to node 1 with weight 7.  You may assume a given topological order corresponding to nodes in increasing order.
Output: The length of a longest path in the graph, followed by a longest path as a sequence of space-separated node labels. (If multiple longest paths exist, you may return any one.)

Sample Input:
0 4
0 1 7
0 2 4
1 4 1
2 3 2
3 4 3

Sample Output:
9
0 2 3 4
'''
import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your LongestPath function here, along with any subroutines you need
# s and t are the starting and the ending nodes of the path respectively
# E[u] is the list of neighbors of the vertex u, paired with corresponding edge weights
# LongestPath should return the length of the longest path betweeen s and t together with
# the list of nodes of the path
def LongestPath(s: int, t: int,
                E: Dict[int, List[Tuple[int, int]]]) -> Tuple[int, List[int]]:
    
    dist, pre = initDist(E)
    #print(E)
    if s in dist:
        dist[s] = 0
    '''
    for u, edges in E.items():
       #le = len(E[key])
        for v, weight in edges:
            if dist[u]!=float('-inf') and dist[v]< dist[u]+weight:
                dist[v] = dist[u]+weight
                pre[v] = u
    '''
    for key in sorted(E.keys()):
        le = len(E[key])
        for i in range(le):
            v = E[key][i][0]
            weight = E[key][i][1]
            if dist[v]< dist[key]+weight:
                dist[v] = dist[key]+weight
                pre[v] = key
   # print(dist)
    if dist[t] == float('-inf'):
      #  print("no path")
        return (float('-inf'), [])
    
    longest = dist[t] 
    curr = t
    path = []
   # print(pre)
    while curr!=None:
        path.append(curr)
        curr = pre[curr]
    path= path[::-1]
    ans = (longest, path)        
    return ans

def initDist(E):
    nodes = set()
    for node in E.keys():
        nodes.add(node)
    
    for edges in E.values():
        for edge in edges:
            dNode = edge[0]
            nodes.add(dNode)
    dist = {}
    pre = {}
    for node in nodes:
        dist[node] = float('-inf')
        pre[node] = None
    return dist, pre
