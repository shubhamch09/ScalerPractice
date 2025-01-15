# check if the given string is a pallendrome or not 

def solve(A, st, end):
    N = len(A)

    while st < end:
        if A[st] != A[end]:
            return False
            
        else:
            st += 1
            end -= 1

    return True




A = "AmadamN"
st = 1
end = 5
print(solve(A,st,end))
    