# Given an integer array of size N print all the start and End index of all subArrays of size K

def solve(A,K):
    N = len(A)
    st = 0
    end = K-1

    while end < N:
        print(st," ", end)
        st +=1
        end+=1




A = [1,2,3,4,5,6,7,8,9,0]
K = 2
solve(A,K)

