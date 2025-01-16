# we are given an array of len N we need to find the max sum of the among all the subarrays.


def solve(A):

    N = len(A)

    maxsum = 0
    currentsum = A[0]


    for i in range( N):
        
        currentsum = max(A[i], currentsum + A[i])

        maxsum = max(currentsum, currentsum)


    return maxsum



