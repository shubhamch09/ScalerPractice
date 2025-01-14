# Print all subarrays of an array in T.C = O(N^3)

def solve(A):
    N = len(A)
    for i in range(N):
        for j in range(i, N):
            st = i 
            end = j
            for k in range(st, end):
                print(A[k], end = " ")
            print()
    return 0

A = [6,3,3,6,7,8,7,3,7]
solve(A)