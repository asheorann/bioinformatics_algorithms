''''
Code Challenge: Solve the Shared k-mers Problem.

Input: An integer k and two strings.
Output: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting positions of these k-mers in the respective strings.

Sample Input:
3
AAACTCATC
TTTCAAATC

Sample Output:
(0, 0)
(4, 2)
(0, 4)
(6, 6)
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your SharedKMers function here, along with any subroutines you need
# ok so this is not working so we are going to use sets to make it faster 

def SharedKMers(k: int, s: str, t: str) -> List[Tuple[int, int]]:
    output = []
    set1 = {}
    l1 = len(s)-k+1
    l2 = len(t)-k+1
    for i in range(l1):
        p = s[i:i+k]
        set1[p] = set1.get(p,0)
        if p in set1:
            set1[p] +=1
        else:
            set1[p] =1
    set2 = {}
    for i in range(l2):
        p = t[i:i+k]
        if p in set2:
            set2[p] +=1
        else:
            set2[p] =1  
    #print(set2.keys())
    for key in set1.keys():
        if key in set2.keys():
            indexs = [i for i in range(l1) if s[i:i+k] == key]
            indext = [i for i in range(l2) if t[i:i+k]==key]
            output.extend([(iss, itt) for iss in indexs for itt in indext])
        
        if reverse_complement(key) in set2.keys():
            #print(reverse_complement(key))
           # print('set2:', set2)
            indexs = [i for i in range(l1) if s[i:i+k] == key]
            indext = [i for i in range(l2) if t[i:i+k]==reverse_complement(key)]
            output.extend([(iss, itt) for iss in indexs for itt in indext])
            #find the index of where the key is in the first and where the reverse is in the second one. 
            #add that tuple to my output
            
    return output

def reverse_complement(pattern: str) -> str:
    """Calculate the reverse complement of a DNA pattern."""
    ns = ""
    l = len(pattern)
    for i in range(l):
        if pattern[i] == 'A':
            ns+='T'
        elif pattern[i] =='C':
            ns+='G'
        elif pattern[i] =='G':
            ns+='C'
        elif pattern[i] =='T':
            ns+='A'
    ns = ns[::-1]
    return ns