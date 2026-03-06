import sys
import heapq


def shortest(node,graph,goal,n):
    visit = [0]*(n+1)
    q=[]
    heapq.heappush(q,(0,node))
    while q:
        cost , cur = heapq.heappop(q)
        if cur==goal:
            return cost
        visit[cur]=1
        for i in graph[cur]:
            if visit[i]==0:
                heapq.heappush(q,(cost+1,i))
                
    
    return -1
n,m =list(map(int,input().split()))
ini,goal=list(map(int,input().split()))
heur={}
graph={}
for _ in range (n):
    key,val =list(map(int,input().split()))
    heur[key]=val
for _ in range (m):

    key,val =list(map(int,input().split()))
    if key not in graph:
        graph[key]=[val]
    else:
        graph[key].append(val)
print(heur,graph)
inadmiss=[]
for i,j in heur.items():
    
    if shortest(i,graph,goal,n)<j:
        inadmiss.append(i)
print (inadmiss)



