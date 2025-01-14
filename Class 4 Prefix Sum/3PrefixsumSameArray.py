def solve(A):
    N = len(A)

    for i in range(1,N):
        A[i] = A[i-1] +A[i]

    return A
