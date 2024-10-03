'''

Squared Error Distortion Problem: Compute the squared error distortion of a set of data points with respect to a set of centers.

Input: A set of points Data and a set of centers Centers.
Output: The squared error distortion Distortion(Data, Centers).
Code Challenge: Solve the Squared Error Distortion Problem.

Input: Integers k and m, followed by a set of centers Centers and a set of points Data.
Output: The squared error distortion Distortion(Data, Centers). Your answer should be accurate to three decimal places.

Sample Input:
2 2
2.31 4.55
5.96 9.08
--------
3.42 6.03
6.23 8.25
4.76 1.64
4.47 4.33
3.95 7.61
8.93 2.97
9.74 4.03
1.73 1.28
9.72 5.01
7.27 3.77

Sample Output:
18.245559999999994
'''

# Insert your SquaredErrorDistortion function here, along with any subroutines you need
import math
def SquaredErrorDistortion(k: int, m: int,
                           Centers: List[Tuple[float, ...]],
                           Data: List[Tuple[float, ...]]) -> float:
    total = 0
    for dataPoint in Data:
        closestCenter = None
        ccDist = float('inf')
        for center in Centers:
            d = distance(dataPoint, center)
            if d<ccDist:
                ccDist = d
                closestCenter = center
        #print(total)
        total +=ccDist**2
    
    n = len(Data)
    distortion = total/n
    return distortion

def distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d +=(p1[i]-p2[i])**2
    dist = math.sqrt(d)
    return dist

'''
Code Challenge: Implement the Lloyd algorithm for k-means clustering.

Input: Integers k and m followed by a set of points Data in m-dimensional space.
Output: A set Centers consisting of k points (centers) resulting from applying the Lloyd algorithm to Data and Centers, where the first k points from Data are selected as the first k centers.

Sample Input:
2 2
1.3 1.1
1.3 0.2
0.6 2.8
3.0 3.2
1.2 0.7
1.4 1.6
1.2 1.0
1.2 1.1
0.6 1.5
1.8 2.6
1.2 1.3
1.2 1.0
0.0 1.9

Sample Output:
1.8 2.8666666666666667
1.0599999999999998 1.1400000000000001

'''

# Insert your Lloyd function here, along with any subroutines you need
import math
def Lloyd(k: int, m: int,
          Data: List[Tuple[float, ...]]) -> List[Tuple[float, ...]]:
    centers = []
    for i in range(k):
        centers.append(Data[i])
    it=0
    while it<30:
        it+=1
        newList = []
        for center in centers:
            temp = []
            count=0
            #we are trying to create a cluster of datapoints called temp
            for dataPoint in Data:
                c = closestCenter(dataPoint, centers)
                if center==c:
                    temp.append(dataPoint)
                    count+=1
            #we find the center of this cluster
            averagePoint =average(temp)
            newList.append(averagePoint)
           # print(newList)
        if newList ==centers:
            return newList
        else:
            centers=newList
            
def closestCenter(point, centers):
    bestDist = float('inf')
    bestCenter = None
    for center in centers:
        dist = distance(point, center)
        if dist<bestDist:
            bestDist = dist
            bestCenter = center
    return bestCenter

def average(temp):
    n = len(temp[0])
    numberOfPoints = len(temp)
    totalPoint = [0 for x in range(n)]
    i=0
    while i<n:
        totali=0
        for point in temp:
            totali += point[i]
        totalPoint[i]=totali
        i+=1
    #print(totalPoint)
    average = [0 for y in range(n)]
    for i in range(n):
        average[i] = totalPoint[i]/numberOfPoints   
    return average

def distance(p1, p2):
    d = 0
    for i in range(len(p1)):
        d +=(p1[i]-p2[i])**2
    dist = math.sqrt(d)
    return dist
