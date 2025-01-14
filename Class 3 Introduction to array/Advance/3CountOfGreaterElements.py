def solve(A):
    count = 0
    max = A[0]

    for i in A:
        if i > max:
            max = i

    for i in A:
        if i < max:
            count+=1
    print(count)
    return count  

A = [5, 5, 3]
solve(A)
A = [1,2,3]
solve(A)