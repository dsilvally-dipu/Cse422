# PROBLEM: Find the shortest possible route that visits each city exactly once 
# and returns to the starting city.
#
# CHALLENGE: Unlike Knapsack (0/1), TSP requires a PERMUTATION of all cities.
# Using standard crossover/mutation would create invalid routes (duplicates).
# We must use:
# 1. SWAP MUTATION: Switch positions of two cities to keep the set the same.
# 2. ORDERED CROSSOVER (OX1): Inherit a segment from one parent and fill the 
#    rest with the other parent's cities in order, skipping duplicates.
# 3. INVERSE FITNESS: Since we want the MINIMUM distance, fitness = 1 / Distance.

import random
import math

cities = [(0, 0), (1, 5), (5, 2), (6, 6), (8, 3),(2, 7), (3, 3), (7, 8), (9, 5), (4, 9)]

def rndpopulation():
    primary=[0,1,2,3,4,5,6,7,8,9]
    random.shuffle(primary)
    return primary

def fitness(arr):
    global cities
    cost =0
    n=len(arr)
    for i in range(n-1):
        x,y=cities[arr[i]]
        x1,y1=cities[arr[i+1]]
        cost += math.sqrt((x-x1)**2 + (y-y1)**2)

    x,y=cities[arr[0]]
    x1,y1=cities[arr[n-1]]
    cost+= math.sqrt((x-x1)**2 + (y-y1)**2)

    return cost

def mutate(arr,mutpercentage):
    arr=arr[:]
    n=len(arr)
    if random.random()< mutpercentage:
        p1=random.randint(0,n-1)
        p2=random.randint(0,n-1)
        arr[p1],arr[p2]=arr[p2],arr[p1]
    return arr

# def two_point_crossover(p1, p2):
#     n = len(p1)

#     i = random.randint(0, n-2)
#     j = random.randint(i+1, n-1)

#     c1 = p1[:i] + p2[i:j] + p1[j:]
#     c2 = p2[:i] + p1[i:j] + p2[j:]

#     return c1, c2

def crossover(arr1, arr2):
    n = len(arr1)

    p1 = n // 3
    p2 = p1 + 3

    child1 = [None] * n
    child2 = [None] * n

    # Copy middle segment
    child1[p1:p2] = arr1[p1:p2]
    child2[p1:p2] = arr2[p1:p2]

    # Fill child1
    current_pos1 = 0
    for item in arr2:
        if item not in child1:
            # Skip the segment
            while p1 <= current_pos1 < p2:
                current_pos1 += 1
            if current_pos1 >= n:
                break

            child1[current_pos1] = item
            current_pos1 += 1

    current_pos2 = 0
    for item in arr1:
        if item not in child2:
            while p1 <= current_pos2 < p2:
                current_pos2 += 1

            if current_pos2 >= n:
                break

            child2[current_pos2] = item
            current_pos2 += 1

    return child1, child2

def garunner():
    genr =10
    popsize=80
    inipop=[rndpopulation() for _ in range ( popsize)]
    # print (inipop)
    stored=[]
    for i in inipop:
        stored.append((i,fitness(i)))
    
    for gen in range (1,genr+1):
        stored.sort(key=lambda x:x[1])
        survivors=stored[:popsize//2]
        best_route, best_dist = survivors[0]
        print(f"Gen {gen} | Best Distance: {best_dist:.2f}")
        
        nextgen_stored=[]
        nextgen_stored.append((best_route,best_dist)) #elitism
        for i in range(len(survivors)):
            for j in range(i+1,len(survivors),5):
                c1,c2=crossover(survivors[i][0],survivors[j][0])
                c11=mutate(c1,.10)
                c22=mutate(c2,.10)
                nextgen_stored.append((c11,fitness(c11)))
                nextgen_stored.append((c22,fitness(c22)))
            if len(nextgen_stored)>popsize:
                break
        stored=nextgen_stored

    return best_route,best_dist
print(garunner())
