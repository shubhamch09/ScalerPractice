def solve( A, B):

    Array = [0] * A
    for st, end, coins in B:
        A[st - 1] = A[st - 1] + coins
        A[end] = -1 * coins + A[end]


    for i in range(1,B):
        Array[i] = Array[i-1] + Array[i]
    return Array




A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

solve(A,B)