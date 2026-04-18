"""
Problem Overview: Minimax Gene Sequence Generator

Goal: 
Implement a Minimax search with Alpha-Beta pruning to generate the best possible 
gene sequence from a given pool of nucleotides.

Game Mechanics:
- MAX and MIN take turns picking nucleotides from the available pool.
- Characters are picked WITHOUT replacement (the pool shrinks each turn).
- The game tree depth is determined by the length of the target sequence.
- Alpha-Beta pruning must be used to optimize the search space.

Utility Calculation:
- Cost = Sum( weight[i] * abs(ord(generated[i]) - ord(target[i])) )
- Utility Score = -Cost (since MAX wants to maximize this negative value, i.e., minimize cost).
- The weights are dynamically assigned using the last N digits of the given 
  Student ID, where N is the length of the target sequence.

Input Format:
Line 1: Comma-separated pool of uppercase letters (e.g., A,T,C,G)
Line 2: The target gene sequence string (e.g., ATGC)
Line 3: Space-separated Student ID (e.g., 1 8 1 0 4 0 5 2)

Output Format:
Line 1: The optimal gene sequence found by the algorithm.
Line 2: The final utility score.
"""



def utility_check(s1,target,weight=[8,8,1,1]):
    cost=0
    for i in range(len(s1)):
        cost+= weight[i]* ( abs( ord(s1[i]) - ord(target[i])))
    return - cost





def minmax(curseq,avl_pool,target,alpha,beta,my_turn):
    if len(curseq)==len(target):
        return utility_check(curseq,target),curseq
    best_seq=""
    if my_turn:
        best=-float('inf')
        for i in range(len(avl_pool)):
            
            c=avl_pool[i]
            new= avl_pool[:i]+avl_pool[i+1:]
            val,seq=minmax(curseq+c,new,target,alpha,beta,False)
            if val>best:
                best=val
                best_seq=seq
            alpha=max(best,alpha)
            if alpha>= beta:
                break
        return best,best_seq

    else:
        best=float('inf')
        for i in range(len(avl_pool)):
            c=avl_pool[i]
            new= avl_pool[:i]+avl_pool[i+1:]
            val,seq=minmax(curseq+c,new,target,alpha,beta,True)
            if val<best:
                best=val
                best_seq=seq
            beta=min(best,beta)
            if alpha>= beta:
                break
        return best,best_seq


    
        



avl_pool="ATCG"
target="GCAT"
id=[1,8,1,0,4,0,5,2]

p=minmax("",avl_pool,target,-float('inf'),float('inf'),True)
print(p)