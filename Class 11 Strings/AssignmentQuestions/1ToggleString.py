# You are given a string and you arfe required to change the case of the each character in the string
def solve(A):
    N = len(A)
    ans = ''
    for i in range(N):
        char = A[i]
        if char.isupper():
            ans +=  char.lower()

        else:
            ans +=  char.upper()

    return ans

A = "Hello"

print(solve(A))