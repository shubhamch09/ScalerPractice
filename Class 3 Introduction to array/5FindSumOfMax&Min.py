def solve(A):
    max = A[0]
    min = A[0]
    N = len(A)
    for i in range(0,N):
        if A[i] < min:
            min = A[i]
        if A[i] >  max:
            max = A[i]

    sum  = max+min
    print(sum)
    return sum 

A = [-2, 1, -4, 5, 3]
solve(A)