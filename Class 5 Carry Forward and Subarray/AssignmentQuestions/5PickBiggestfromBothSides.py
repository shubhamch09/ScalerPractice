def maximum_removed_sum(A, B):
    N = len(A)
    
    # Compute prefix sums
    prefix_sum = [0] * (B + 1)
    for i in range(B):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]
    
    print(prefix_sum)
    # Compute suffix sums
    suffix_sum = [0] * (B + 1)
    for i in range(B):
        suffix_sum[i + 1] = suffix_sum[i] + A[N - i - 1]
    print(suffix_sum)
    # Compute the maximum possible sum
    max_sum = float("-inf")
    for i in range(B + 1):
        print(prefix_sum[i], suffix_sum[B-i])
        max_sum = max(max_sum, prefix_sum[i] + suffix_sum[B - i])
    print(max_sum)
    return max_sum




A = [1, 2, 3, 4, 5, 6, 7]
B = 3
print(maximum_removed_sum(A, B))