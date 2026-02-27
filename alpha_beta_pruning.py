def alpha_beta(values,tree,node,alpha,beta,depth,mmaxi_player):
    if depth==0 or len(tree[node])==0:
        return values[node]
    if mmaxi_player:
        maxv=float('-inf')
        for i in tree[node]:
            eval=alpha_beta(values,tree,i,alpha,beta,depth-1,False)
    
            maxv=max(maxv,eval)
            alpha=max(alpha,maxv)
            if alpha>=beta:
                break
        return maxv
    else:
        minv=float('inf')
        
        for i in tree[node]:
            eval=alpha_beta(values,tree,i,alpha,beta,depth-1,True)
    
            minv=min(minv,eval)
            beta=min(minv,beta)
            if alpha>=beta:
                break
        return minv


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
values = {
    'D': 3,
    'E': 5,
    'F': 6,
    'G': 9
}
result = alpha_beta(values,tree,'A', 3, float('-inf'), float('inf'), True)
print(result)