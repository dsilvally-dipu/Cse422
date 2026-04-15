# Array[10,5,8,2]# two players# both play optimally# only choose from leftmost or rightmost
# first person wants maximum total value



def solve(arr,l,r,my_turn):
    if l>r : return 0
    left=arr[l]
    right = arr[r]

    if my_turn:
        op1=left + solve(arr,l+1,r,False)
        op2=right + solve(arr,l,r-1,False)
        return max(op1,op2)
    
    else :
        op1= solve(arr,l+1,r,True)
        op2= solve(arr,l,r-1,True)
        return min(op1,op2)
    


print(solve([10,5,8,2],0,3,True))
# solve(0,3,True)   on [10,5,8,2]    MAX
# ├── op1 = 10 + solve(1,3,False)
# │   └── solve(1,3,False)   on [5,8,2]    MIN
# │       ├── op1 = solve(2,3,True)
# │       │   └── solve(2,3,True)   on [8,2]    MAX
# │       │       ├── op1 = 8 + solve(3,3,False)
# │       │       │   └── solve(3,3,False)   on [2]    MIN
# │       │       │       ├── op1 = solve(4,3,True) = 0
# │       │       │       ├── op2 = solve(3,2,True) = 0
# │       │       │       └── return min(0,0) = 0
# │       │       │
# │       │       ├── op2 = 2 + solve(2,2,False)
# │       │       │   └── solve(2,2,False)   on [8]    MIN
# │       │       │       ├── op1 = solve(3,2,True) = 0
# │       │       │       ├── op2 = solve(2,1,True) = 0
# │       │       │       └── return min(0,0) = 0
# │       │       │
# │       │       └── return max(8+0, 2+0) = max(8,2) = 8
# │       │
# │       ├── op2 = solve(1,2,True)
# │       │   └── solve(1,2,True)   on [5,8]    MAX
# │       │       ├── op1 = 5 + solve(2,2,False)
# │       │       │   └── solve(2,2,False) = 0
# │       │       │   └── value = 5 + 0 = 5
# │       │       │
# │       │       ├── op2 = 8 + solve(1,1,False)
# │       │       │   └── solve(1,1,False)   on [5]    MIN
# │       │       │       ├── op1 = solve(2,1,True) = 0
# │       │       │       ├── op2 = solve(1,0,True) = 0
# │       │       │       └── return min(0,0) = 0
# │       │       │   └── value = 8 + 0 = 8
# │       │       │
# │       │       └── return max(5,8) = 8
# │       │
# │       └── return min(8,8) = 8
# │
# ├── op2 = 2 + solve(0,2,False)
# │   └── solve(0,2,False)   on [10,5,8]    MIN
# │       ├── op1 = solve(1,2,True)
# │       │   └── solve(1,2,True) = 8
# │       │
# │       ├── op2 = solve(0,1,True)
# │       │   └── solve(0,1,True)   on [10,5]    MAX
# │       │       ├── op1 = 10 + solve(1,1,False)
# │       │       │   └── solve(1,1,False) = 0
# │       │       │   └── value = 10 + 0 = 10
# │       │       │
# │       │       ├── op2 = 5 + solve(0,0,False)
# │       │       │   └── solve(0,0,False)   on [10]    MIN
# │       │       │       ├── op1 = solve(1,0,True) = 0
# │       │       │       ├── op2 = solve(0,-1,True) = 0
# │       │       │       └── return min(0,0) = 0
# │       │       │   └── value = 5 + 0 = 5
# │       │       │
# │       │       └── return max(10,5) = 10
# │       │
# │       └── return min(8,10) = 8
# │
# └── return max(10+8, 2+8) = max(18,10) = 18