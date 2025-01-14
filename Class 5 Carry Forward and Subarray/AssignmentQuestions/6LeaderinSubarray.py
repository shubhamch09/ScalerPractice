# find the number of leaders in the array
# # Approach 1 : T.C = O(N^2)

def solve(A):
    N = len(A)
    ans = 0

    resultarray = []    
    for i in range(N):
        for j in range(i+1, N):
            
            if A[i] < A[j]:
                ans += 1
                print(A[i], A[j], ans)
                
        if ans == 0:
            resultarray.append(A[i])
        else:
            ans = 0
    return resultarray

A = [16, 17, 4, 3, 5, 2]
print(solve(A))
