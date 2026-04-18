# Problem: The Poisoned Treasure Line
#
# Two players take treasures from either end.
# On each turn, a player may take one or two treasures from the same end.
# But if a player takes two treasures in one turn,
# then on their next turn they are forced to take only one.
# Both players play perfectly.
# Find the maximum score the first player can guarantee.
def solve(arr, l, r, my_turn, must_take_one):

    if l > r:
        return 0

    # MAX player
    if my_turn:
        best = -float('inf')

        # take 1 from left
        best = max(best, arr[l] + solve(arr, l+1, r, False, False))

        # take 1 from right
        best = max(best, arr[r] + solve(arr, l, r-1, False, False))

        # take 2 (only if allowed)
        if not must_take_one and l+1 <= r:
            # left side
            best = max(best, arr[l] + arr[l+1] + solve(arr, l+2, r, False, True))
            # right side
            best = max(best, arr[r] + arr[r-1] + solve(arr, l, r-2, False, True))

        return best

    # MIN player
    else:
        best = float('inf')

        # take 1 from left
        best = min(best, solve(arr, l+1, r, True, False))

        # take 1 from right
        best = min(best, solve(arr, l, r-1, True, False))

        # take 2 (only if allowed)
        if not must_take_one and l+1 <= r:
            best = min(best, solve(arr, l+2, r, True, True))
            best = min(best, solve(arr, l, r-2, True, True))

        return best
    

arr = [10, 5, 8, 2]

print(solve(arr, 0, len(arr)-1, True, False))