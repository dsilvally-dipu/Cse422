def solve(arr, l, r, my_turn, alpha=float('-inf'), beta=float('inf'), depth=0):
    if l > r:
        return 0, alpha, beta

    if my_turn:
        best = float('-inf')

        val1, _, _ = solve(arr, l+1, r, False, alpha, beta, depth+1)
        op1 = arr[l] + val1
        best = max(best, op1)
        alpha = max(alpha, best)

        if alpha >= beta:
            return best, alpha, beta

        val2, _, _ = solve(arr, l, r-1, False, alpha, beta, depth+1)
        op2 = arr[r] + val2
        best = max(best, op2)
        alpha = max(alpha, best)

        return best, alpha, beta

    else:
        best = float('inf')

        val1, _, _ = solve(arr, l+1, r, True, alpha, beta, depth+1)
        best = min(best, val1)
        beta = min(beta, best)

        if alpha >= beta:
            return best, alpha, beta

        val2, _, _ = solve(arr, l, r-1, True, alpha, beta, depth+1)
        best = min(best, val2)
        beta = min(beta, best)

        return best, alpha, beta