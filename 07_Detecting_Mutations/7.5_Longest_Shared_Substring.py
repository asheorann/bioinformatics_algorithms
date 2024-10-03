'''
Longest Shared Substring Problem: Find the longest substring shared by two strings.

Input: Strings Text1 and Text2.
Output: The longest substring that occurs in both Text1 and Text2.

Sample Input:
TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA

Sample Output:
CTC
'''

import sys
from typing import List, Dict, Iterable, Tuple

def longest_shared_substring(text1: str, text2: str) -> str:
    text1= text1+"$"
    patterns1=[]
    for i in range(len(text1)):
        patterns1.append(text1[i:])
    patterns2 = []
    for i in range(len(text2)):
        patterns2.append(text2[i:])   
    #patterns=patterns1+patterns2
    trie = TrieConstruction(patterns1)
    #print(trie)
    bestS= ""
    bestList = []
    for pattern in patterns2:
        matched = matching(pattern, trie)
        bestList.append(matched)
    for t in bestList:
        if len(t)>len(bestS):
            bestS=t
    #print(bestS)
    return bestS
    #now we have to label the nodes
def matching(text, trie):
    index = 0
    v = 0
    matchedText = ""
    while True:
        leaf = True
        for t in trie:
            if t[0]==v:
                leaf=False
                break
        if leaf:
            return matchedText
        found = False
        for t in trie:
            if v==t[0] and index <len(text) and text[index]==t[2]:
                v=t[1]
                matchedText += t[2]
                index+=1
                found = True
                break
        if not found:
            return matchedText
            
def findSuffix(trie):
    pass

def TrieConstruction(Patterns: List[str]) -> List[Tuple[int, int, str]]:
    trie = []
    for pattern in Patterns:
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
    return trie
 