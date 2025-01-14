def solve( A, B):
    N = len(A)

    # Range function does not include the last value. that is why N and not N-1
    for i in range(0,N):
        
        for j in range(0,N):
            print(i , j)
            C = A[i] + A[j]
            print(C)
            if i != j and B == C:
                
                return 1
    return 0

solve([1,2,3,4], 7)