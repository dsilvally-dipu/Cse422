import sys 
import heapq
sys.stdin = open("input1.txt","r")

def sol():
    n,m=list(map(int,input().split()))
    ep1,ep2=list (map(int ,input().split()))
    en1,en2=list(map(int,input().split()))
    maze=[input() for _ in range (n)]
    
    q=[]
    moves = [(0,1),(1,0),(-1,0),(0,-1)]
    vst = [[0]*m for _ in range(n)]
    heapq.heappush(q,[0,0,ep1,ep2,""]) # cost ,heur
    step=0
    while q:
        cost,heur,s1,s2,path=heapq.heappop(q)
        vst[s1][s2]=1
        step+=1
        if s1==en1 and s2==en2:
            print(len(path),path)
            return
        for i,j in moves:
            new1=s1+i
            new2=s2+j
            
            if 0<=new1<n and 0<=new2<m and vst[new1][new2]==0 and  maze[new1][new2]!= "#":
                
                if (i,j)==(0,1):
                    st="R"
                elif (i,j)==(1,0):
                    st="D"
                elif (i,j)==(-1,0):
                    st="U"
                else:
                    st="L"
                heurstic = abs (new1-en1)+abs (new2-en2)
                heapq.heappush(q,[cost+heurstic+1,heurstic,new1,new2,path+st])
    print("-1")




        



test=int(input())
for i in range(test):
    sol()
