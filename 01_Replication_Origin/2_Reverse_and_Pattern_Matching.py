import sys

# Please do not remove package declarations because these are used by the autograder.
# Insert your reverse_complement function here, along with any subroutines you need

#Reverse Complement Problem: Find the reverse complement of a DNA string.
#Input: A DNA string Pattern.
#Output: Patternrc , the reverse complement of Pattern.

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

#Input: Two strings, Pattern and Genome.
#Output: A collection of integers specifying all starting positions where Pattern appears as a substring of Genome.

def pattern_matching(pattern: str, genome: str) -> list[int]:
    """Find all occurrences of a pattern in a genome."""
    p = len(pattern)
    l = len(genome)
   # reverse = reverse_complement(pattern)
    starts = []
    for i in range(l-p+1):
        if genome[i:i+p] == pattern:
            starts.append(i)
      #  elif genome[i:i+p] == reverse:
       #     starts.append(i)
    return starts
        