def solve(A):

    N = len(A)
    prefix_sum = [0] * N
    prefix_sum[0] = A[0]

    for i in range(1,N):
        prefix_sum[i] = prefix_sum[i-1] +A[i]

    
    count = -1

    for i in range(N):

        if i == 0:
            sum_left = 0
            sum_right = prefix_sum[N-1]
        else:
            sum_left = prefix_sum[i-1]
            sum_right = prefix_sum[N-1] - prefix_sum[i]

        if i == (N-1):
            sum_left = prefix_sum[N-1]
            sum_right = 0
        else:
            sum_left = prefix_sum[i-1]
            sum_right = prefix_sum[N-1] - prefix_sum[i]

        if sum_left == sum_right:
            count = i

    return count