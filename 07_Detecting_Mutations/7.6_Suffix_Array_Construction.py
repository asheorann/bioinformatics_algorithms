'''
Suffix Array Construction Problem: Construct the suffix array of a string.

Input: A string Text.
Output: SuffixArray(Text).

Sample Input:
AACGATAGCGGTAGA$

Sample Output:
15 14 0 1 12 6 4 2 8 13 3 7 9 10 11 5
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your suffix_array function here, along with any subroutines you need
def suffix_array(text: str) -> List[int]:
    """
    Generate the suffix array for the given text.
    """
    suffixes = {}
    array = []
    for i in range(len(text)):
        s = text[i:]
        suffixes[s] =i
        #print(suffixes)
    #lets sort it now
    sortedS = dict(sorted(suffixes.items(),key=lambda x:x[0]))
    suffixes = sortedS
    for value in suffixes.values():
        array.append(value)
    return array

#