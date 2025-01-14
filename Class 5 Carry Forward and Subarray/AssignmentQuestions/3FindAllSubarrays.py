def solve( A):
    N = len(A)
    resultarray = []
    for i in range(0,N):
        for j in range(i,N):
            subarray = []
            for k in range(i ,j+1):
                subarray.append(A[k])
            resultarray.append(subarray)
    print(resultarray)
    return resultarray




A = [1,2,3]
solve(A)