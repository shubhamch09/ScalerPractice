def solve( A, B, C):
    subarray = []
    for i in range(B, C + 1):
        subarray.append(A[i])
    
    return subarray
A = [1,2,3,4,5,6,7,8,9]
B = 0
C = 6

solve(A,B,C)