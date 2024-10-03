'''
Code Challenge: Implement TrieMatching to solve the Multiple Pattern Matching Problem.

Input: A string Text and a space-separated collection of strings Patterns.
Output: All starting positions in Text where a string from Patterns appears as a substring. You may assume that no string from Patterns is a prefix of another string from Patterns.

Sample Input:
AATCGGGTTCAATCGGGGT
ATCG GGGT

Sample Output:
ATCG: 1 11
GGGT: 4 15
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your trie_matching function here, along with any subroutines you need
def trie_matching(text: str, patterns: List[str]) -> Dict[str, List[int]]:
    """
    Find all starting positions in Text where a string from Patterns appears as a substring.
    """
    matches ={}
    for pattern in patterns:
        matches[pattern] = []
    trie = TrieConstruction(patterns)
    for i in range(len(text)):
        matched = matching(text[i:], trie)
        if matched!="No":
            length = matched[1]
            p = matched[0]
            location = i
            if p in matches:
                matches[p].append(i)
            else:
                matches[p] = [i]         
    return matches
#i want the output of this to be ["pattern", int:length] or "No"

def matching(text, trie):
    #symbol = text[0]
    index = 0
    symbol = text[index]
    v = 0
    while True:
        leaf = True
        for t in trie:
            if t[0]==v:
                leaf = False
        if leaf==True:
            output =""
            curr = v
            while curr!=0:
                for t in trie:
                    if t[1]==curr:
                        output+=t[2]
                        curr = t[0]
            pattern = output[::-1]
            return [pattern, len(pattern)]
        else:
            found = False
            for t in trie:
                if v==t[0] and symbol==t[2]:
                    v=t[1]
                    index+=1
                    if index<len(text):
                        symbol = text[index]
                    found = True
                    break
            if not found:
                return "No" 
                               
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