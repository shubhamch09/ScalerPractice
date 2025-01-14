# Reverse the given string

def solve(A):

    N = len(A)
    reverseString = ''
    
    for i in range(N-1,-1,-1):
        reverseString += A[i]


    return reverseString


A = "Shubham"
print(solve(A))