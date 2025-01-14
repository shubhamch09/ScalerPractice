def solve(A):
    count = len(A)
    N = len(A) 
    minimum = A[0]
    maximum = A[0]

    for i in range(0,N):
        if A[i] > maximum:
            maximum = A[i]
        if A[i] < minimum:
            minimum = A[i]
    
    print(maximum )
    print(minimum) 
    minindex = -1
    maxindex = -1
    if maximum == minimum:
        return 1
    for i in range(N):
        if A[i] == maximum:
            maxindex = i
            if minindex != -1:
                count = min(count , i - minindex + 1 )
        if A[i] == minimum:
            minindex = i
            if maxindex != -1:
                count = min(count, i - maxindex + 1)
        print(count)


    return count


A = [814,761,697,483,981]
solve(A)

                



