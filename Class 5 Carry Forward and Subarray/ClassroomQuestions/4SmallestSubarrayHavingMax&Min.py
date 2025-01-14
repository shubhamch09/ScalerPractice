# given an array of size N , return the smallest subarray having both min and max of the array. 
# Observations : if min and max both are same then return 1
# to get the smallest subarray we only need one min and one max element
# position of min and max should be at the corners of the subarray

# Brute Force Approach : find min and max 
# If (A[i] == min )  --> need to look for closest max element
# if (A[i] == max )  --> need to look for closest min element
# T.C = O(N^2)

def solve(A):
    N = len(A)
    minn = min(A)
    maxx = max(A)
    ans = N
    if minn == maxx:
        return 1
    for i in range(N):
        if A[i] == minn:
            for j in range(i, N):
                if A[j] == maxx:
                    ans = min(ans, j - i + 1)
                    print(A[i], A[j], ans)
                    break
        if A[i] == maxx:
            for j in range(i, N):
                if A[j] == minn:
                    ans = min(ans, j - i + 1)
                    print(A[i], A[j], ans)
                    break

    return ans


# Approach 2 : using Carry Forward Technique
# Find the min and max element of the array
# Find the first occurence of min and max element from left and right
# find the minimum of the two
# T.C = O(N)

def solve(A):
    N = len(A)
    minn = min(A)
    maxx = max(A)
    if minn == maxx:
        return 1
    
    ans = N
    minn_index = -1
    maxx_index = -1
    # itrating from right to left
    for i in range(N-1, -1, -1):
        if A[i] == minn:
            minn_index = i
            print(A[i], minn_index)
            if maxx_index != -1:
                ans = min(ans, maxx_index - minn_index + 1)

        if A[i] == maxx:
            maxx_index = i
            print(A[i], maxx_index)
            if minn_index != -1:
                ans = min(ans, minn_index - maxx_index + 1)
    return ans



A = [6,3,3,6,7,8,7,3,7]
print(solve(A)) # 3