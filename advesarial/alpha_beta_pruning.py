# def alpha_beta(values,tree,node,alpha,beta,depth,mmaxi_player):
#     if depth==0 or len(tree[node])==0:
#         return values[node]
    
#     for i in tree[node]:
#             if alpha>=beta : return alpha if mmaxi_player else beta
#             eval=alpha_beta(values,tree,i,alpha,beta,depth-1,not mmaxi_player)
#             if mmaxi_player and alpha<eval:alpha=eval
#             elif not mmaxi_player and beta>eval: beta =eval
            
            
#     return alpha if mmaxi_player else beta


# tree = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': [],
#     'F': [],
#     'G': []
# }
# values = {
#     'D': 3,
#     'E': 5,
#     'F': 6,
#     'G': 9
# }
# result = alpha_beta(values,tree,'A', 3, float('-inf'), float('inf'), True)
# print(result)










#new way 
# def alpha_beta(data,alpha,beta,flag): #flag true max level
#     if len(data)==1:
#         return data[0]
#     mid =len(data)//2
#     for i in [data[:mid],data[mid:]]:
#         if alpha>=beta :return alpha if flag else beta 
#         res=alpha_beta(i,alpha,beta,not flag)
#         if flag and alpha<res : alpha =res
#         elif not flag and beta>res : beta =res
#     return alpha if flag else beta
# data =[5,12,7,3,2,8,4,6]
# p=alpha_beta(data,float('-inf'), float('inf'),True)
# print(p)












#another
def minmax_tree(data, alpha, beta, my_turn):

    if len(data) == 1:
        return data[0], [data[0]]
    mid = len(data) // 2
    best_seq = []
    if my_turn:  # MAX
        best = -float('inf')
        for child in [data[:mid], data[mid:]]:
            val, seq = minmax_tree(child, alpha, beta, False)
            if val > best:
                best = val
                best_seq = seq
            alpha = max(alpha, best)

            if alpha >= beta:
                break
        return best, best_seq

    else:  # MIN
        best = float('inf')
        for child in [data[:mid], data[mid:]]:

            val, seq = minmax_tree(child, alpha, beta, True)
            if val < best:
                best = val
                best_seq = seq
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best, best_seq
    
data = [5,12,7,3,2,8,4,6]

print(minmax_tree(data, float('-inf'), float('inf'), True))
