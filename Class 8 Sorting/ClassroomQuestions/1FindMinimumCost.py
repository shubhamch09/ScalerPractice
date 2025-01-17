# Given an array A find to minimum cost to remove all the elements from the array


def solve(A):
    N = len(A)
    A.sort(reverse = True)


    cost = 0

    for i in range(N):

        cost = cost +  (A[i] * (i+1)) 

    return cost


A = [4,6,1]
print(solve(A))
    