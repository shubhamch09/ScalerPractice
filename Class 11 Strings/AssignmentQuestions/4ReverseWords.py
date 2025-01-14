# reverse the words in the string

def solve(A):

    words = A.split()

    words.reverse()

    return " ".join(words)



A = "This is string"
print(solve(A))