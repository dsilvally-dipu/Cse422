import sys

n,m = map(int,input().split())
ini,goal = map(int,input().split())

heur={}
graph={}

for _ in range(n):
    key,val = map(int,input().split())
    heur[key]=val

for _ in range(m):
    key,val = map(int,input().split())

    if key not in graph:
        graph[key]=[val]
    else:
        graph[key].append(val)

print(heur,graph)

inconsistent=[]

for u in graph:
    for v in graph[u]:

        if heur[u] > 1 + heur[v]:
            inconsistent.append(u)

print(inconsistent)