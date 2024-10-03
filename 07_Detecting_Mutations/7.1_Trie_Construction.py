'''
Code Challenge: Solve the Trie Construction Problem.

Input: A space-separated collection of strings Patterns.
Output: The adjacency list corresponding to Trie(Patterns), in the following format. If Trie(Patterns) has n nodes, first label the root with 0 and then label the remaining nodes with the integers 1 through n - 1 in any order you like. Each edge of the adjacency list of Trie(Patterns) will be encoded by a triple: the first two members of the triple must be the integers labeling the initial and terminal nodes of the edge, respectively; the third member of the triple must be the symbol labeling the edge.

Sample Input:
ATAGA ATC GAT

Sample Output:
0 1 A
0 7 G
1 2 T
2 3 A
2 6 C
3 4 G
4 5 A
7 8 A
8 9 T
'''

import sys
from typing import List, Dict, Iterable, Tuple, Set

# Please do not remove package declarations because these are used by the autograder.

# Insert your TrieConstruction function here, along with any subroutines you need
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
         