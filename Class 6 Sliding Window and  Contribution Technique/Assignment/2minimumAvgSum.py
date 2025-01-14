def solve( A, B):      
    N = len(A)
    resultavg = float("inf")
    currentsum = 0
    returnindex = 0
    for i in range(B):
        currentsum += A[i]
    resultavg = min(resultavg, currentsum/B)
    print(currentsum,resultavg)
    st = 1
    end = B
    while end < N:
        currentsum = currentsum - A[st -1] + A[end]
        avg = currentsum/B
        print(currentsum,avg,st )
        if resultavg > avg:
            resultavg = avg
            returnindex = st      
        st += 1
        end += 1
    print(returnindex)
    return returnindex



A = [18,11,16,19,11,9,8,15,3,10,9,20,1,19]
B = 1

solve(A,B)