# find the longest pallendrome substring from the given string


def solve(A):
    N = len(A)
    maxpallindrome = float("-inf")
    for i in range(N):
        for j in range(i,N):


            st = i
            end = j
            blnUpdateMax = True
            while st < end:
                if A[i] != A[j]:
                    blnUpdateMax = False
                else:
                    blnUpdateMax = True
                st += 1
                end -= 1
            
                if blnUpdateMax:
                    maxpallindrome = max (maxpallindrome, j -i +1)



    return maxpallindrome



A = "AmadamN"

print(solve(A))
