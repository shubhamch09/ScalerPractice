def solve (A,B):
    N = len(A)
    psum = []
    for i in range(1,N):
        A[i] = A[i-1] + A[i]

    for L, R in B:
        if L == 0:
            sum = A[R]
        else:
            sum = A[R] - A[L-1] 
        psum.append(sum)
    
    print(psum)
    return psum
A = [2, 2, 2]
B = [[0, 0], [1, 2]]
solve(A,B)