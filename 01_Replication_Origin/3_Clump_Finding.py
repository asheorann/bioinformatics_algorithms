import sys

# Please do not remove package declarations because these are used by the autograder.
# Insert your find_clumps function here, along with any subroutines you need

#Clump Finding Problem: Find patterns forming clumps in a string.
#Input: A string Genome, and integers k, L, and t.
#Output: All distinct k-mers forming (L, t)-clumps in Genome.
#Sample Input:
#CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA
#5 50 4
#Sample Output: GAAGA CGACA
def frequent_words(text: str, k: int) -> list[str]:
    """Find the most frequent k-mers in a given text."""
    frequentPatterns = []
    freqMap = {}
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        if pattern in freqMap:
            freqMap[pattern]+=1
        else:
            freqMap[pattern] = 1
    maxValue = max(freqMap.values())
    for p, v in zip(freqMap.keys(), freqMap.values()):
        if v == maxValue:
            frequentPatterns.append(p)
    return freqMap

def find_clumps(genome: str, k: int, l: int, t: int) -> list[str]:
    """Find patterns forming clumps in a genome."""
    patterns = []
    n = len(genome)
    grange= n-l+1
    #print(grange)
    for i in range(grange):
        w = genome[i: i+l]
        freqMap = frequent_words(w, k)
        for s in freqMap:
            if freqMap[s] >= t:
                patterns.append(s)
    #patterns = list(set(patterns))
    return list(set(patterns))

