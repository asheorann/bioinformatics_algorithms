'''
Burrows-Wheeler Transform Construction Problem: Construct the Burrows-Wheeler transform of a string.

Input: A string Text.
Output: BWT(Text).

Sample Input:
GCGTGCCTGGTCA$

Sample Output:
ACTGGCT$TGCGGC
'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.

# Insert your burrows_wheeler_transform function here, along with any subroutines you need
def burrows_wheeler_transform(text: str) -> str:
    """
    Generate the Burrows-Wheeler Transform of the given text.
    """
    
    rotations = []
    for i in range(len(text)):
        r = text[i:]+text[:i]
        rotations.append(r)
   # print(rotations)
    rotations = sorted(rotations)
    answer = ""
    for a in rotations:
       value =a[-1]
       answer+=value
    return answer

'''
Inverse Burrows-Wheeler Transform Problem: Reconstruct a string from its Burrows-Wheeler transform.

Input: A string Transform (with a single "
$
$" symbol).
Output: The string Text such that BWT(Text) = Transform.

Sample Input:
TTCCTAACG$A

Sample Output:
TACATCACGT$
'''

import sys
from typing import List, Dict, Iterable, Tuple

def inverse_burrows_wheeler_transform(transform: str) -> str:
    a = lexo(transform)
    newInput = addSubscript(transform)
    lex = addSubscript(a)
  #  longL = len(transform)*2
    m = createMatrix(lex, newInput)   
    l = len(m[0])
    draft = invert(m) 
    lastD = delSubscript(draft)
    final = lastD[1:]+lastD[0]
    return final

def lexo(transform):
    new = transform
    inp = ''.join(sorted(new))
    return inp

def invert(m):
    final = m[0][0]
    latest = m[0][0]
    visited = []
    visited.append(m[0][0])
    while len(visited)<len(m):
        for i in range(len(m)):
            if latest==m[i][1]:
                final+=m[i][0]
                latest = m[i][0]
                visited.append(m[i][0])
    return final

def addSubscript(transform):
    counts={}
    ans=""
    for a in transform:
        if a in counts:
            counts[a]+=1
        else:
            counts[a]=1
        ans+=a+str(counts[a])
    return ans

def delSubscript(draft):
    #print(len(draft))
    new = ""
    for i in range(len(draft)):
        if draft[i] in "$ACGT":
            new += draft[i]
    return new

#this also works
def createMatrix(lex, transform):
    rotations = []
    lexR = split(lex)
    lexSR =set(lexR)
    #print("length of lexR", len(lexSR))
    transformR = split(transform)
    transformSR = set(transformR)
    #print(len(transformSR))
    for i in range(len(lexR)):
        add = [lexR[i], transformR[i]]
        rotations.append(add)
 
    return rotations 
#this also works 
def split(text):
    rot = []
    curr = 0
    while curr < len(text):
        t = ""
        if curr<len(text) and text[curr] in "$ACGT":
            t += text[curr]
            curr += 1
            while curr<len(text) and text[curr] not in "$ACGT":
                t += text[curr]
                curr += 1
        rot.append(t)
    return rot

'''
Code Challenge: Implement BWMatching.

Input: A string BWT(Text), followed by a space-separated collection of Patterns.
Output: A space-separated list of integers, where the i-th integer corresponds to the number of substring matches of the i-th member of Patterns in Text.

Sample Input:
TCCTCTATGAGATCCTATTCTATGAAACCTTCA$GACCAAAATTCTCCGGC
CCT CAC GAG CAG ATC

Sample Output:
2 1 1 0 1
'''

def bw_matching(bwt, Patterns):
    a = lexo(bwt)
    count = 0
    newInput = addSubscript(bwt)
    lex = addSubscript(a)
    m = createMatrix(lex, newInput)   
    ltf = lastToFirst(m)
    counts = []
    for pattern in Patterns:
        count = findCount(m, ltf, pattern)
        counts.append(count)
    return counts

def findCount(m, ltf, pattern):
    top = 0
    bottom =len(m)
    while top<=bottom:
        if len(pattern)!=0:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            found = False
            positions = []
            for i in range(top, bottom+1, 1):
                if i<len(m) and symbol in m[i][1]:
                    firstp = ltf[i]
                    found = True
                    positions.append(firstp)
            if found==False:
                return 0
            top = min(positions)         
            bottom =max(positions)
        if len(pattern)==0: 
            return bottom-top+1

def lastToFirst(m):
    ltf = {}
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][1]==m[j][0]:
                ltf[i]=j
    return ltf

def lexo(transform):
    new = transform
    inp = ''.join(sorted(new))
    return inp

def addSubscript(transform):
    counts={}
    ans=""
    for a in transform:
        if a in counts:
            counts[a]+=1
        else:
            counts[a]=1
        ans+=a+str(counts[a])
    return ans

def createMatrix(lex, transform):
    rotations = []
    lexR = split(lex)
    lexSR =set(lexR)
    transformR = split(transform)
    transformSR = set(transformR)
    for i in range(len(lexR)):
        add = [lexR[i], transformR[i]]
        rotations.append(add)
 
    return rotations 

def split(text):
    rot = []
    curr = 0
    while curr < len(text):
        t = ""
        if curr<len(text) and text[curr] in "$ACGTPANAMASBANA":
            t += text[curr]
            curr += 1
            while curr<len(text) and text[curr] not in "$ACGTPANAMASBANAS":
                t += text[curr]
                curr += 1
        rot.append(t)
    return rot