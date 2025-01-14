def solve(A):
    result = 0
    countA = 0
    N = len(A)

    for i in range(0, N):
        if A[i] == 'A':
            countA += 1
        if A[i]== 'G':
            result += countA
        print(result)
    return result







A = "ASDFGAG"
solve(A)