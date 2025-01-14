# we need to count the total umber of subarrays from the given Array A having sum less than B

def solve(A,B):

    N = len(A)
    count = 0
    for i in range(N):
        sum = 0 
        for j in range(i,N):
            sum+= A[j]

            if sum < B:
                count+=1

    return count



A = [1, 11, 2, 3, 15]
B = 10
print(solve(A,B))


