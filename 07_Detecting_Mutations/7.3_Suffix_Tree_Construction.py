'''
Code Challenge: Solve the Suffix Tree Construction Problem.

Input: A string Text.
Output: A list of the edge labels of SuffixTree(Text). You may return these strings in any order.

Sample Input:
ATAAATG$

Sample Output:
A
T
G$
$
T
A
AAATG$
G$
AAATG$
G$
ATG$
TG$
'''
import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your suffix_tree function here, along with any subroutines you need
def suffix_tree(text: str) -> List[str]:
    patterns = []
    for i in range(len(text)):
        patterns.append(text[i:])
    trie = makeTrie(patterns)
    tree = compressTree(trie)
    edges = edgesTree(tree)
    counts = countOutgoing(trie)
 #   print("COUNTS:", counts)
    return edges

def edgesTree(compressed):
    edges = []
    for x in compressed:
        edges.append(x[2])
    return edges    
def compressTree (tree):
    compressed = []
    visited = []
    counts = countOutgoing(tree)
    for node in tree:
        curr, nextN, symbol = node
        
        countInVisited = visited.count(curr)
        if countInVisited==counts[curr]:
            continue
        visited.append(curr)
        if nextN in counts and counts[nextN] ==1:
            startCurr = curr
            while nextN in counts and (counts[nextN]==1):
                for t in tree:
                    if t[0]==nextN:
                        visited.append(nextN)
                        nextN= t[1]
                        symbol+=t[2]
                        break
            add = (curr, nextN, symbol)
            compressed.append(add)
        else:
            compressed.append((curr, nextN, symbol))       
    return compressed 

def countOutgoing(trie):
    counts = {}
    for x in trie:
        curr = x[0]
        if curr in counts:
            counts[curr]+=1
        else:
            counts[curr]=1
    return counts

def makeTrie(patterns):
    trie = []
    for pattern in patterns:
        curr = 0
        for i in range(len(pattern)):         
            symbol = pattern[i]
            found = False
            for t in trie:
                if t[0]==curr and t[2]==symbol:
                    curr = t[1]
                    found = True
                    break
            if found==False:
                if len(trie)!=0:
                    latest = trie[-1][1]+1
                else:
                    latest =1              
                addNode = (curr, latest, symbol)
                trie.append(addNode)
                curr = addNode[1]
    #print("TRIE", trie)
    return trie
