'''

Code Challenge: Implement the FarthestFirstTraversal clustering heuristic (reproduced below).
Input: Integers k and m followed by a set of points Data in m-dimensional space.
Output: A set Centers consisting of k points (centers) resulting from applying FarthestFirstTraversal(Data, k), where the first point from Data is chosen as the first center to initialize the algorithm.

Sample Input:
3 2
0.0 0.0
5.0 5.0
0.0 5.0
1.0 1.0
2.0 2.0
3.0 3.0
1.0 2.0

Sample Output:
0.0 0.0
5.0 5.0
0.0 5.0
'''

import sys
from typing import List, Dict, Iterable, Tuple
import math

# Please do not remove package declarations because these are used by the autograder.

# Insert your FarthestFirstTraversal function here, along with any subroutines you need
def FarthestFirstTraversal(k: int, m: int,
                           Data: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
    centers = []
    centers.append(Data[0])
    dists = {}
    while len(centers)<k:
        maxDist = 0
        maxPoint = None
        for j in range(len(Data)):
            #currDist = 0
            minDist  = float('inf')
            for i in range(len(centers)):
                currDist = distance(centers[i], Data[j])
                if currDist<minDist:
                    minDist = currDist
            dists[Data[j]] = minDist
        for key,v in dists.items():
            if v>maxDist:
                maxDist = v
                maxPoint = key
        centers.append(maxPoint)
      #  print("out of while loop")
        if len(centers)>k:
            break
        
    return centers

def distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d +=(p1[i]-p2[i])**2
    dist = math.sqrt(d)
    return dist