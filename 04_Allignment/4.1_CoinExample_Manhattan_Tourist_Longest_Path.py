'''
Code Challenge: Solve the Change Problem. The DPChange pseudocode is reproduced below for your convenience.

Input: An integer money and an array Coins = (coin1, ..., coind).
Output: The minimum number of coins with denominations Coins that changes money.

Sample Input:
7
1 5

Sample Output:
3
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your Change function here, along with any subroutines you need
def Change(money: int, Coins: List[int]) -> int:
    minNumCoins = {}
    minNumCoins[0] = 0
    for m in range(1, money+1):
        minNumCoins[m] = float('inf')
        l= len(Coins)-1
        for coin in Coins:
            if m>= coin:
                if (minNumCoins[m-coin]+1)<minNumCoins[m]:
                    minNumCoins[m] = (minNumCoins[m-coin]+1)
    return minNumCoins[money]

'''
Code Challenge: Find the length of a longest path in the Manhattan Tourist Problem.

Input: Integers n and m, followed by an n × (m + 1) matrix Down and an (n + 1) × m matrix Right. The two matrices are separated by the "-" symbol.
Output: The length of a longest path from source (0, 0) to sink (n, m) in the rectangular grid whose edges are defined by the matrices Down and Right.

Sample Input:
4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2

Sample Output:
34
'''

# Please do not remove package declarations because these are used by the autograder.

# Insert your LongestPathLength function here, along with any subroutines you need
def LongestPathLength(n: int, m: int,
                      Down: List[List[int]], Right: List[List[int]]) -> int:
    s = [[0 for x in range(m+1)] for y in range(n+1)]
    s[0][0] = 0
    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + Down[i-1][0]
    
    for j in range(1,m+1):
        s[0][j] = s[0][j-1]+ Right[0][j-1]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j]+Down[i-1][j], s[i][j-1]+Right[i][j-1])
    return s[n][m]