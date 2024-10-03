'''

2-Break Sorting Problem: Find a shortest transformation of one genome into another by 2-breaks.

Input: Two genomes with circular chromosomes on the same set of synteny blocks.
Output: The sequence of genomes resulting from applying a shortest sequence of 2-breaks transforming one genome into the other.

Sample Input:
(+1 +2 +3 +4 +5 +6)
(+1 -3 -6 -5)(+2 -4)

Sample Output:
(+1 +2 +3 +4 +5 +6)
(+1 +2 +3 +4 -6 -5)
(+1 +2 -4 -3 -6 -5)
(+1 -3 -6 -5)(+2 -4)

'''

import sys
from typing import List, Dict, Iterable, Tuple

# Please do not remove package declarations because these are used by the autograder.
genome_cycles_t = List[Tuple[int, int]]
# Insert your TwoBreakSorting function here, along with any subroutines you need
def TwoBreakSorting(P: genome_cycles_t, Q: genome_cycles_t) -> List[genome_cycles_t]:
    transform = []
    cycleP=ColoredEdges(P)
    cycleQ=ColoredEdges(Q)
    indices = findUnresolved(cycleP,cycleQ)
  #  print("CycleQ:", cycleQ)
    #print("CycleP:", cycleP)
    transform.append(GraphToGenome(cycleP))
    cyclePL = cycleP.copy()
    cycleQL = cycleQ.copy()
    cn = CycleNumber(cyclePL, cycleQL)
    count=0
    #print("cn:", cn)
    r = False   
    while count<100:
        count+=1
        #print(indices)
     #   print("P at start", cycleP)
        if cycleP==cycleQ:
            break
        indices = findUnresolved(cycleP,cycleQ)
       # print(indices)
        if indices==None:
      #      print("indicies are None")            
            r=True
            break
        else:
           # print(indices)
            edgeQ = cycleQ[indices[0]]
            edgeP1 = cycleP[indices[1]]

            #so now iterate through to find where edge[1]
            for i, edgeP2 in enumerate(cycleP):
                if edgeP2[0]==edgeQ[1]:
                        index = i
                        break
                elif edgeP2[1]==edgeQ[1]:
                        index=i
                        break       
            edgeP2 = cycleP[index]
          #  print("edgeQ:", edgeQ, "edgeP1:", edgeP1, "edgeP2:", edgeP2)
            if edgeQ[0]==edgeP1[1] and edgeQ[1]==edgeP2[1]:
                cycleP = TwoBreakOnGenomeGraph(cycleP, edgeP1[1], edgeP1[0], edgeP2[1], edgeP2[0])
            elif edgeQ[0]==edgeP1[1] and edgeQ[1]==edgeP2[0]:
                cycleP = TwoBreakOnGenomeGraph(cycleP, edgeP1[1], edgeP1[0], edgeP2[0], edgeP2[1])
            elif edgeQ[0]==edgeP1[0] and edgeQ[1]==edgeP2[1]:
                cycleP = TwoBreakOnGenomeGraph(cycleP, edgeP1[0], edgeP1[1], edgeP2[1], edgeP2[0])
            elif edgeQ[0]==edgeP1[0] and edgeQ[1]==edgeP2[0]:
                cycleP = TwoBreakOnGenomeGraph(cycleP, edgeP1[0], edgeP1[1], edgeP2[0], edgeP2[1])
            cyclePLL = cycleP.copy()
            cycleQLL = cycleQ.copy()
            cpa = CycleNumber(cyclePLL, cycleQLL)
          #  print("changed cycle number:", cpa)
        #    print("cycleP:", cycleP)
          #  print("cycleQ:", cycleQ)
          #  print("after",cycleP)
         #   print("original Q:", cycleQ)
            #transform cycleP to genome and add it to the list
            temp = GraphToGenome(cycleP)
            transform.append(temp)
    return transform

def findUnresolved(cycleP, cycleQ):
    for i, edgeQ in enumerate(cycleQ):
      #  print("edgeQ:",edgeQ)
        v0 = edgeQ[0]
        v1 = edgeQ[1]
        unresolved = True
        for j, edgeP1 in enumerate(cycleP):
            if edgeP1[0] == v0 and edgeP1[1] != v1:
                return [i, j]
            elif edgeP1[1] == v0 and edgeP1[0] != v1:
                return [i, j]
    return None     
 
def ColoredEdges(P: List[List[int]]) -> List[Tuple[int, int]]:
    edges = []
    for chromosome in P:
        nodes = ChromosomeToCycle(chromosome)
        n = len(nodes)
        for i in range(1,n,2):
            if  i==(n-1):
                edge = (nodes[n-1], nodes[0])
                edges.append(edge)
                break
            else:
                edge = (nodes[i], nodes[i+1])
                edges.append(edge)
    return edges  
                       
def ChromosomeToCycle(Chromosome: List[int]) -> List[int]:
    output = []

    for i in range(len(Chromosome)):
        j = (abs(Chromosome[i])-1)*2+1
        if Chromosome[i]>0:
            output.append(j)
            output.append(j+1)
        else:
            output.append(j+1)
            output.append(j)
    return output

def TwoBreakOnGenomeGraph(GenomeGraph: genome_cycles_t,
                          i1: int, i2: int, i3: int, i4: int) -> genome_cycles_t:
    #GenomeGraph = [List(x) for x in len(GenomeGraph)]
    #look for i1 in all the elements
    index1=0
    index2=0
    for i in range(len(GenomeGraph)):
        if GenomeGraph[i][0]==i1 and GenomeGraph[i][1]==i2:
            index1=i
        elif GenomeGraph[i][1]==i1 and GenomeGraph[i][0]==i2:
            index1=i
        if GenomeGraph[i][0]==i3 and GenomeGraph[i][1]==i4:
            index2=i
        elif GenomeGraph[i][1]==i3 and GenomeGraph[i][0]==i4:
            index2=i
        
    GenomeGraph[index1]= [i1,i3]
    GenomeGraph[index2]=[i2, i4]
    #GenomeGraph=[Tuple(x) for x in range(len(GenomeGraph))]  
    return GenomeGraph
def GraphToGenome(GenomeGraph: list[Tuple[int, int]]):
    GenomeGraph= [list(c) for c in GenomeGraph]
    cycles = []
    P=[]
    while GenomeGraph:
        start = GenomeGraph[0][0]
        stop = partnerCode(start)
        cycle = []
        curr =start
        edge1=GenomeGraph[0]
        while curr!=stop:
        #for i, edge  in enumerate(GenomeGraph): 
            cycle.append(curr)
            ne = neighbour(curr, edge1)
            curr = ne
            cycle.append(curr)
            index = GenomeGraph.index(edge1)
            GenomeGraph.pop(index)
            partner = partnerCode(curr)
            for x, edge in enumerate(GenomeGraph):
                if partner in edge:
                    curr = partner
                    edge1 = edge
                    break
        cycles.append(cycle)
   # print(cycles)
    for a in cycles:
        genome = CycleToChromosome(a)
        P.append(genome)
    return P
def CycleToChromosome(Nodes: List[int]) -> List[int]:
    output= []
    start = Nodes[0]
    curr =start
    for i in range(0,len(Nodes),2):
        curr = Nodes[i]
        partner = partnerCode(curr)
        if i==0:
            behind=Nodes[-1]
        else:
            behind=Nodes[i-1]
        ahead = Nodes[i+1]
        if partner%2==0 and partner==behind:
            output.append(-partner//2)
        elif partner%2==0 and partner==ahead:
            output.append(partner//2)
        elif partner%2==1 and partner==behind:
            output.append(curr//2)
        elif partner%2==1 and partner==ahead:
            output.append(-curr//2)       
    return output    

def partnerCode(curr):
    if curr%2==1:
        partner=curr+1
    else:
        partner=curr-1
    return partner

def neighbour(curr, edge):
    neighbour = 0
    if curr==edge[0]:
        neighbour = edge[1]
    elif curr==edge[1]:
        neighbour=edge[0]
    return neighbour

def CycleNumber(cyclePL, cycleQL) -> int:
    
    cycleQ = cycleQL.copy()
    cycleP=cyclePL.copy()
    
    cycleCount=0
    while cyclePL and cycleQL:
        start = cyclePL[0][0]
        curr = cyclePL[0][1]
        index = 0
        indexj=0
        cyclePL.pop(0)
        while curr!=start: 
            for i in range(len(cycleQ)):
                if cycleQL[i][0]==curr:
                    curr =cycleQL[i][1]
                    index=i
                    break
                elif cycleQL[i][1]==curr:
                    curr =cycleQL[i][0]
                    index=i
                    break
            cycleQL.pop(index)
            for j,edge in enumerate(cyclePL):
                if edge[0]==curr:
                    curr = edge[1]
                    cyclePL.pop(j)
                    break
                elif edge[1] == curr:
                    curr = edge[0]
                    cyclePL.pop(j)
                    break
            #cyclePL.pop(indexj)
        cycleCount+=1
           
    return cycleCount