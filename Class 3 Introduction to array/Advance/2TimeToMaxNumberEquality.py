def solve(A):
    count = 0
    max = A[0]
    for i in A:
        if i > max:
            max = i
        
    for i in A:
        c = max - i
        count += c
    print(count)
    return count


A = [2, 4, 1, 3, 2]
solve(A)