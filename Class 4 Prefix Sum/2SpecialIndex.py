def solve(A):
    N = len(A)
    prefix_even = [0] * N
    prefix_odd =  [0] * N

    for i in range(N):
        if i == 0:
            if i % 2 == 0:
                prefix_even[i] = A[i]
                prefix_odd[i] = 0

            else:
                prefix_even[i] = 0
                prefix_odd[i] = A[i]

        else:
            if i % 2 == 0:
                prefix_even[i] = prefix_even[i-1] + A[i]
                prefix_odd[i] = prefix_odd[i-1]

            else:
                prefix_even[i] = prefix_even[i-1]
                prefix_odd[i] = prefix_odd[i-1] + A[i]

        
        count = 0

    for i in range(N):
        if i > 0:
            sum_even = prefix_even[i-1] + (prefix_odd[N-1] - prefix_odd[i])
            sum_odd = prefix_odd[i-1] +  (prefix_even[N-1] - prefix_even[i])
        else:
            sum_even = prefix_even[N-1]
            sum_odd = prefix_odd[N-1]
        if sum_even == sum_odd:
            count += 1

    return count
                
        