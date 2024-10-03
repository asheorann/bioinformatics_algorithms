'''
Longest Repeat Problem: Find the longest repeat in a string.

Input: A string Text.
Output: A longest substring of Text that appears in Text more than once.

Sample Input:
ATATCGTTTTATCGTT

Sample Output:
TATCGTT
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your longest_repeat function here, along with any subroutines you need
def longestPath(tree):
    visited = []
    counts = countOutgoing(tree)
    currText = ""
    bestL = 0
    bestS = ""
    nodes = []
    nodes = [(node, "", 0) for node in tree if node[0]==0]
    while nodes:
        node, currText, currL = nodes.pop()
        currText += node[2]
        currL +=len(node[2])
        if node[1] not in counts:
            if currL>bestL:
                bestL = currL
                bestS = currText
        else:
            for t in tree:
                if t[0]==node[1]:
                    nodes.append((t, currText, currL))
    return bestS
        
def suffix_tree(text: str) -> List[str]:
    text = text+"$"
    patterns = []
    for i in range(len(text)):
        patterns.append(text[i:])
    trie = makeTrie(patterns)
    tree = compressTree(trie)
    return tree
def leafsAreBranched(tree):
    visited = []
    counts=countOutgoing(tree)
    curr= 0
    newTree = []
    nextN=0
    for node in tree:
        nextN=node[1]
        while nextN in counts:
            for t in tree:
                if t[0]==curr:
                    nextN=t[1]
        leaf=nextN
        for t in tree:
            if t[1]==leaf:
                visited.append(t)
    for node in tree:
        if node in tree and node not in visited:
            newTree.append(node)
    #print("VISITED",visited)
    return newTree

def longest_repeat(text):
    firstTree = suffix_tree(text)
    tree = leafsAreBranched(firstTree)
    path = longestPath(tree)
    return path               
  
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